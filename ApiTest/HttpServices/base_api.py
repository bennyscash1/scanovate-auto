from dataclasses import asdict, fields
from typing import Any, Dict, Type, TypeVar

T = TypeVar("T")

class BaseDTO:
    @classmethod
    def from_dict(cls: Type[T], data: Dict[str, Any]) -> T:
        kwargs = {}
        for f in fields(cls):
            value = data.get(f.name)
            if value is None:
                kwargs[f.name] = None
            else:
                kwargs[f.name] = f.type(value)
        return cls(**kwargs)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
