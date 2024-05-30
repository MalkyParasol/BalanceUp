"""
userRouter.py

This module defines API routes related to user management, including signing up, signing in, retrieving user details by ID, and updating user profiles.

"""
from fastapi import FastAPI, Depends, APIRouter, HTTPException
from BalanceUp.Backend.app.db_management.user_CRUD import create_user, get_user_by_id, get_user_by_name_password, \
    update_user
from BalanceUp.Backend.app.models.userModel import User
from bson import ObjectId

from BalanceUp.Backend.utils.logDecorator import log_to_file

userRouter = APIRouter()


@userRouter.get("/{id}")
@log_to_file()
def getUserById(_id: str):
    """
        Retrieve user details by user ID.

        Args:
            id (str): The unique identifier of the user.

        Returns:
            User: A User object representing the retrieved user.
        """
    try:
        user_id = ObjectId(_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user id")

    user = get_user_by_id(user_id)

    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@userRouter.post("/signUp")
@log_to_file()
def signUp(user: User):
    """
        Sign up a new user.

        Args:
            user (User): A User object representing the details of the user to be signed up.

        Returns:
            dict: A dictionary containing the inserted user ID if successful, or an error message if failed.
    """
    inserted_id = create_user(user)
    if inserted_id:
        return {"inserted_id": str(inserted_id)}
    else:
        return {"message": "Failed to sign up user."}


@userRouter.post("/signIn")
@log_to_file()
def signIn(name: str, password: str):
    """
        Sign in a user.

        Args:
            name (str): The username of the user.
            password (str): The password of the user.

        Returns:
            dict: A dictionary containing the user ID if the sign-in was successful, or an error message if failed.
    """
    user_id = get_user_by_name_password(name, password)
    if user_id:
        return {"userId": str(user_id)}  # Convert ObjectId to string for JSON response
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


@userRouter.put("/{id}")
@log_to_file()
def setProfile(Id: str, user: User):
    """
       Update user profile.

       Args:
           id (str): The unique identifier of the user.
           user (User): A User object representing the updated details of the user.

       Returns:
           dict: A dictionary containing a success message if the update was successful.
    """
    try:
        user_id = ObjectId(Id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user id")
    try:
        update_user(user_id, user)
        return {"message": "User profile updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="failed to update the user")
