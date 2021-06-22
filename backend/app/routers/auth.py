from datetime import datetime, timedelta

import bcrypt
from fastapi import Depends, HTTPException, APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.models.models import User
from app.db import session
from app.models.schemas import LoginSchema

router = APIRouter()

class Settings(BaseModel):
    authjwt_secret_key: str = "dcd50ec763c0610b2f6095cb2107146bb8b81fbeb178e6ed5b4852ae0a12b33b"
    # Configure application to store and get JWT from cookies
    authjwt_token_location: set = {"cookies"}
    # Only allow JWT cookies to be sent over https
    authjwt_cookie_secure: bool = False
    # Enable csrf double submit protection. default is True
    authjwt_cookie_csrf_protect: bool = False
    # Change to 'lax' in production to make your website more secure from CSRF Attacks, default is None
    # authjwt_cookie_samesite: str = 'lax'

@AuthJWT.load_config
def get_config():
    return Settings()


def get_hashed_password(password: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def check_password(user_password: str, hashed_password: str):
    return bcrypt.checkpw(user_password.encode(), hashed_password.encode())

@router.post("/login")
async def login(
    data: LoginSchema,
    Authorize: AuthJWT = Depends(),
):
    try:
        user = session.query(User).filter(User.email == data.email).first()
        if not user:
            raise HTTPException(status_code=400, detail="アカウントが見つかりません")
        if not check_password(data.password, user.password):
            raise HTTPException(status_code=400, detail="アカウントが見つかりません")


        access_token = Authorize.create_access_token(
            subject=user.id,
            expires_time=timedelta(days=30),
        )
        refresh_token = Authorize.create_refresh_token(subject=user.id)

        Authorize.set_access_cookies(access_token)
        Authorize.set_refresh_cookies(refresh_token)

        return {"message": "Successfully login"}
    except HTTPException as exc:
        return HTTPException(status_code=400, detail=exc.detail)

# FIXME: 認証周りの疎通確認用コード(必要なければ削除)
@router.get("/users/me")
def get_current_user(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        user_id = Authorize.get_jwt_subject()
        return {"user_id": user_id}

    except HTTPException as exc:
        return HTTPException(status_code=400, detail=exc.details)
