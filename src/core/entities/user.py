from datetime import datetime
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    is_active: bool = True
    
    class Config:
        from_attributes = True