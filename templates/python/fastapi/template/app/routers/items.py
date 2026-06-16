from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from ..dependencies import get_db  # example dependency

router = APIRouter(prefix="/items", tags=["items"])

class ItemCreate(BaseModel):
    name: str
    price: float

class ItemOut(BaseModel):
    id: int
    name: str
    price: float

@router.post("/", response_model=ItemOut)
async def create_item(item: ItemCreate, db=Depends(get_db)):
    # In real template: use service or repository
    # For skeleton, just echo
    return {"id": 1, "name": item.name, "price": item.price}

@router.get("/{item_id}", response_model=ItemOut)
async def get_item(item_id: int, db=Depends(get_db)):
    if item_id != 1:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, "name": "Example", "price": 9.99}