from datetime import datetime
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True