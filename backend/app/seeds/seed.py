import bcrypt
import datetime

from app.db import session
from app.models.models import User

def get_hashed_password(password: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def seed():
    password_digest = get_hashed_password("password")
    user1 = User(name="user1",
                 email="user1@example.com",
                 password=password_digest,
                 created_at=datetime.datetime.now()
                 )
    session.add(user1)
    session.commit()

if __name__ == "__main__":
    seed()
