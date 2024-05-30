"""
test_userRouter.py

This module contains unit tests for the user router endpoints.

"""

from BalanceUp.Backend.app.models.userModel import User
from BalanceUp.Backend.app.routers.userRouter import getUserById, signUp, signIn, setProfile


def testGetUserById():
    """
        Test case for the getUserById endpoint.

        It tests whether user details can be successfully retrieved by user ID.

    """
    user = User(name="Malkala", password="12345", email="malky5885@gmail.com", phone="0548545885")
    result = getUserById("664ef396319b8c6690e4f211")
    assert result == user


def testSignUp():
    """
       Test case for the signUp endpoint.

       It tests whether a new user can be successfully signed up.

    """
    user = User(name="Yisrael", password="Yisrael41566", email="Yisra@gmail.com", phone="0556656565")
    result = signUp(user)
    assert result != {"message": "Failed to sign up user."}
    assert "inserted_id" in result


def testSignIn():
    """
       Test case for the signIn endpoint.

       It tests whether a user can successfully sign in with valid credentials.

    """
    result = signIn("Malka", "12345")
    assert result == {"userId": "664ef396319b8c6690e4f211"}


def testSetProfile():
    """
        Test case for the setProfile endpoint.

        It tests whether a user profile can be successfully updated.

    """
    user = User(name="Malkala", password="12345", email="malky5885@gmail.com", phone="0548545885")
    result = setProfile("664ef396319b8c6690e4f211", user)
    assert result == {"message": "User profile updated successfully"}
