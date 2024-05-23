from pydantic import ValidationError

from app.models.userModel import User
from app.db_management.connectDB import db

users = db['users']


# Function to get users
def get_users():
    allUsers = []
    for user_data in users.find():
        try:
            user = User(**user_data)
            allUsers.append(user)
        except ValidationError as e:
            print(f"Skipping invalid user data: {e}")
    return allUsers


# Function to post a new user
def post_user(user: User):
    try:
        user_data = user.dict()
        users.insert_one(user_data)
        print("User inserted successfully.")
    except ValidationError as e:
        print(f"Failed to insert user: {e}")


def get_user_by_name_password(name: str, password: str) -> User:
    user_data = users.find_one({"name": name, "password": password})
    if user_data:
        return User(**user_data)
    else:
        return None


def get_user_by_id(user_id: int) -> User:
    user_data = users.find_one({"id": user_id})
    if user_data:
        return User(**user_data)
    else:
        return None

#צריך לעשות middleware שבודק האם המשתמש עשה login או signin אחרת הוא לא יכול לבצע שום פעולה ואפשר לבדוק את זה אם ה get_current_user() = None

# צריך לעשות מזהה משתמש רץ

# צריך לעשות גיבוב לסיסמא של המשתמש