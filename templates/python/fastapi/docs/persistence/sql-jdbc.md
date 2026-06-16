# General SQL / JDBC-like Patterns with FastAPI (Python)

While we prefer SQLAlchemy for most cases (see postgresql.md), for raw control or legacy integration use:

- `aiosqlite` or `asyncpg` directly with `databases` library or raw `asyncpg`.
- Or stick with SQLAlchemy Core for performance-critical queries.

## Example with asyncpg (low-level)

```python
import asyncpg

async def get_connection():
    return await asyncpg.connect("postgresql://...")

async def fetch_items():
    conn = await get_connection()
    try:
        return await conn.fetch("SELECT id, name FROM items")
    finally:
        await conn.close()
```

## Recommendations
- Always use parameterized queries.
- Connection pooling via the library (SQLAlchemy has good support).
- For transactions in async code, use `async with` context.

This complements the JPA-style in postgresql.md and keeps parity with the Java module's sql-jdbc.md.