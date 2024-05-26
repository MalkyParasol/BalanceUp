from bson import ObjectId
from pydantic import ValidationError
from BalanceUp.Backend.app.db_management.connectDB import get_db
from BalanceUp.Backend.app.models.userModel import User

db = get_db()
users_collection = db['users']


def create_user(user: User) -> ObjectId | None:
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
    user_data = users_collection.find_one({"name": name, "password": password})
    if user_data:
        return user_data["_id"]
    else:
        return None


def get_user_by_id(user_id: ObjectId) -> User | None:
    user_data = users_collection.find_one({"_id": user_id})
    if user_data:
        return User(**user_data)
    else:
        return None


def update_user(user_id: ObjectId, user: User):
    users_collection.update_one({"_id": user_id}, {"$set": user.dict()})

#צריך לעשות middleware שבודק האם המשתמש עשה login או signin אחרת הוא לא יכול לבצע שום פעולה ואפשר לבדוק את זה אם ה get_current_user() = None

# צריך לעשות מזהה משתמש רץ

# צריך לעשות גיבוב לסיסמא של המשתמש
