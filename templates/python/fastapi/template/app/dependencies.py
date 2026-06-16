# Example dependencies for FastAPI template
from typing import AsyncGenerator
import asyncpg  # or from sqlalchemy.ext.asyncio

# Placeholder for DB session / connection
async def get_db() -> AsyncGenerator[object, None]:
    # In real app: yield a session from SQLAlchemy async engine or Motor client
    db = "mock_db_connection"  # replace with real pool
    try:
        yield db
    finally:
        # cleanup
        pass

# Auth example, etc.
