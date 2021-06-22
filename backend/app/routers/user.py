import bcrypt
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.db import session
from app.models.models import User
from app.models.schemas import LoginSchema

router = APIRouter()

