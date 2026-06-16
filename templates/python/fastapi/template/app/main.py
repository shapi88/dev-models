from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting Python 3 + FastAPI template (dev-models reference)")
    yield
    # Shutdown
    print("Shutting down")

app = FastAPI(title="Python FastAPI Template", lifespan=lifespan, version="0.1.0")

@app.get("/health")
async def health():
    return {"status": "ok", "framework": "fastapi", "python": "3.12+"}

# Add your routers here
# from .routers import items
# app.include_router(items.router)