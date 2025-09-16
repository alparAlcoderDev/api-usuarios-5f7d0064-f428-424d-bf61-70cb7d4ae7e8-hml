from fastapi import APIRouter, Depends, HTTPException
from typing import List
from core.entities.item import Item
from core.usecases.item import ItemUseCase
from infrastructure.database.session import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/items", tags=["Itens"])

@router.get("/", response_model=List[Item])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ItemUseCase(db).get_items(skip, limit)

@router.post("/", response_model=Item)
def create_item(item: Item, db: Session = Depends(get_db)):
    return ItemUseCase(db).create_item(item)