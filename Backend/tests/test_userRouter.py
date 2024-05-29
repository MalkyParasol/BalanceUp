import pytest
from bson import ObjectId
from fastapi import HTTPException
from unittest.mock import patch

from BalanceUp.Backend.app.models.userModel import User
from BalanceUp.Backend.app.routers.userRouter import getUserById, signUp, signIn, setProfile


def testGetUserById():
    user = User(name="Malkala", password="12345", email="malky5885@gmail.com", phone="0548545885")
    result = getUserById("664ef396319b8c6690e4f211")
    assert result == user




def testSignUp():
    user = User(name="Yisrael", password="Yisrael41566", email="Yisra@gmail.com", phone="0556656565")
    result = signUp(user)
    assert result != {"message": "Failed to sign up user."}
    assert "inserted_id" in result


def testSignIn():
    result = signIn("Malka", "12345")
    assert result == {"userId": "664ef396319b8c6690e4f211"}


def testSetProfile():
    user = User(name="Malkala", password="12345", email="malky5885@gmail.com", phone="0548545885")
    result = setProfile("664ef396319b8c6690e4f211", user)
    assert result == {"message": "User profile updated successfully"}


