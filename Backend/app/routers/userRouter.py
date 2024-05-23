from fastapi import FastAPI, Depends, APIRouter, HTTPException
from app.db_management.user_CRUD import get_users, post_user, get_user_by_name_password, get_user_by_id
from app.models.userModel import User
from utils.userUtil import update_current_user, get_current_user

userRouter = APIRouter()

currentUser = None


@userRouter.get("")
def getUser():
    return get_current_user()


@userRouter.post("/signUp")
def signUp(user: User):
    post_user(user)
    return {"message": "User created successfully"}


@userRouter.post("/signIn")
def signIn(name: str, password: str):
    user = get_user_by_name_password(name, password)
    if user:
        update_current_user(user)
        return {"message": "Sign-in successful", "userId": user.id}
    else:
        return {"message": "Invalid name or password"}



