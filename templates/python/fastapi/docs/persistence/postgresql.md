# PostgreSQL with FastAPI (SQLAlchemy 2.0 + async)

## Recommended Stack

- `sqlalchemy[asyncio]`
- `asyncpg` driver
- `alembic` for migrations (preferred over raw SQL scripts for this stack)

## Example

```python
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine("postgresql+asyncpg://...")
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase): pass

class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
```

Use `async with AsyncSessionLocal() as session:` in dependencies or services.

## Migration

Use Alembic with async support.

See the monolith-to-microservices guide for data ownership when splitting services.