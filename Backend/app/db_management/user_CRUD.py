from bson import ObjectId
from pydantic import ValidationError
from BalanceUp.Backend.app.db_management.connectDB import get_db
from BalanceUp.Backend.app.models.userModel import User

db = get_db()
users_collection = db['users']


def create_user(user: User) -> ObjectId | None:
    """
        Creates a new user record in the database.

        Args:
            user (User): A User object representing the details of the user.

        Returns:
            ObjectId | None: The unique identifier of the newly created user record in the database,
                or None if creation fails.
    """
    try:
        insert_result = users_collection.insert_one(user.dict())
        if insert_result.inserted_id:
            return insert_result.inserted_id
        else:
            return None
    except ValidationError as e:
        print(f"Failed to insert user: {e}")
        return None


def get_user_by_name_password(name: str, password: str) -> ObjectId | None:
    """
       Retrieves a user record from the database by name and password.

       Args:
           name (str): The username of the user.
           password (str): The password of the user.

       Returns:
           ObjectId | None: The unique identifier of the retrieved user record in the database,
               or None if the user does not exist.
       """
    user_data = users_collection.find_one({"name": name, "password": password})
    if user_data:
        return user_data["_id"]
    else:
        return None


def get_user_by_id(user_id: ObjectId) -> User | None:
    """
       Retrieves a user record from the database by its ID.

       Args:
           user_id (ObjectId): The unique identifier of the user record.

       Returns:
           User | None: A User object representing the retrieved user record, or None if not found.
       """
    user_data = users_collection.find_one({"_id": user_id})
    if user_data:
        return User(**user_data)
    else:
        return None


def update_user(user_id: ObjectId, user: User):
    """
       Updates an existing user record in the database.

       Args:
           user_id (ObjectId): The unique identifier of the user record to be updated.
           user (User): A User object containing the updated details of the user.
       """
    users_collection.update_one({"_id": user_id}, {"$set": user.dict()})


