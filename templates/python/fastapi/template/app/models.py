from pydantic import BaseModel

class Item(BaseModel):
    id: int | None = None
    name: str
    price: float

# In a full template, also define SQLAlchemy models or Beanie documents here or in a separate domain layer.