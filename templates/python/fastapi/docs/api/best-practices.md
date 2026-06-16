# FastAPI API Best Practices (Python 3)

## Keep Routers Thin

```python
from fastapi import APIRouter, Depends
from app.dependencies import get_current_user
from app.services import ItemService

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=ItemOut)
async def create_item(
    data: ItemCreate,
    service: ItemService = Depends(),
    user=Depends(get_current_user),
):
    return await service.create(data, user)
```

## Use Pydantic v2 Models

- `BaseModel` for request/response
- `Field` for validation and examples
- `model_config` for JSON schema tweaks

## Versioning

Path-based (recommended for consistency with the Java module):
- `/api/v1/items`
- `/api/v2/items`

## Error Handling

Use `HTTPException` + custom exception handlers that return consistent Problem-Detail-like responses (or use fastapi-problem or similar).

## OpenAPI / Docs

FastAPI auto-generates excellent docs. Enhance with:
- `response_model`
- `responses` dict for error cases
- `summary` / `description` on operations

See the Java `rest-controller-best-practices.md` for philosophy — the same "thin controller, rich service" principle applies.