"""Simple configuration.

In real projects consider pydantic-settings or dynaconf.
"""
from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = "myapp"
    debug: bool = False


settings = Settings()