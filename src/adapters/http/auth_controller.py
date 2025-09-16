from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from core.entities.user import User
from core.usecases.auth import AuthUseCase
from infrastructure.database.session import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/auth", tags=["Autenticação"])
security = HTTPBearer()

@router.post("/register", response_model=User)
def register(user: User, db: Session = Depends(get_db)):
    return AuthUseCase(db).register_user(user)

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    return AuthUseCase(db).login(username, password)