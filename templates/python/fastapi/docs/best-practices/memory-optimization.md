# Memory & Startup Optimization — FastAPI / Python 3

## Memory

- Use `uvicorn --workers N` or `gunicorn` with appropriate worker count (not too high).
- Prefer async code paths to reduce thread memory.
- Be careful with large in-memory caches; use Redis where possible.
- Profile with `memory_profiler` or `py-spy`.

## Startup Time

- Use `lifespan` events instead of heavy top-level imports.
- Lazy-load heavy dependencies inside functions or with `Depends`.
- For production: pre-warm with a small request or use `--preload` carefully.
- Consider `python -m compileall` or bytecode caching in containers.

## FastAPI + Uvicorn Specific

```bash
# Good production command
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4 --loop uvloop
```

See the Java memory and startup guides for the cross-cutting principles (many translate directly).