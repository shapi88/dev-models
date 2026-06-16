# Monolith to Microservices Migration for Python + FastAPI

This module-specific note supplements the cross-cutting guide in `manual/java-25-spring-boot-4/migration/monolith-to-microservices.md` (or the shared architectures docs).

## Python + FastAPI Specifics

- Use FastAPI's APIRouter for internal "module" boundaries before extraction.
- For service extraction: FastAPI + Uvicorn can be deployed independently easily.
- Async nature makes event-driven migration (using asyncio, or libraries like aio-pika / aiokafka) natural.
- Data access: When splitting, move SQLAlchemy engines or Motor clients to the new service. Use outbox pattern for reliable events.
- Memory/Startup: The optimization docs in this module (memory-optimization.md, startup-time-optimization.md) become critical once you have many small FastAPI services.
- Template: Start new microservices from the `template/` in this module.

Follow the general strategy (Strangler Fig, identify bounded contexts first, database per service) but adapt communication to async where possible for Python's strengths.

See the main migration guide for the full step-by-step.