from typing import Any, Protocol

# This is our adapter interface

class Config(Protocol):
    def get(self, key: str) -> Any | None:
        ...