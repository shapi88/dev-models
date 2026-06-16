# Persistence for Python + FastAPI

- [PostgreSQL (SQLAlchemy async)](./postgresql.md)
- [MongoDB (Motor / Beanie)](./mongodb.md)

General principle: each bounded context (see architectures) should own its data store. Use the monolith-to-microservices migration guide when splitting.