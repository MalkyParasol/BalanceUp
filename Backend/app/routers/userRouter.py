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
    inserted_id = create_user(user)
    if inserted_id:
        return {"inserted_id": str(inserted_id)}
    else:
        return {"message": "Failed to sign up user."}


@userRouter.post("/signIn")
@log_to_file()
def signIn(name: str, password: str):
    user_id = get_user_by_name_password(name, password)
    if user_id:
        return {"userId": str(user_id)}  # Convert ObjectId to string for JSON response
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


@userRouter.put("/{id}")
@log_to_file()
def setProfile(Id: str, user: User):
    try:
        user_id = ObjectId(Id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user id")
    try:
        update_user(user_id, user)
        return {"message": "User profile updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="failed to update the user")
