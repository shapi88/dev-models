# MongoDB with FastAPI

## Recommended

- `motor` (async MongoDB driver) or `beanie` (ODM on top of Motor + Pydantic).

## Example with Motor + Pydantic

```python
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["mydb"]
items = db["items"]

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
async def create(item: Item):
    result = await items.insert_one(item.model_dump())
    return {"id": str(result.inserted_id)}
```

Prefer Beanie for more "Spring Data JPA"-like experience with Pydantic models.