from typing import Optional


class Tag:
    def __init__(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
    ):
        self.id = id or 0
        self.set_name(name or "")

    def set_name(self, name: str):
        self.name = name

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def to_string(self):
        return f"Id: {self.get_id()} | Nome: {self.get_name()}"
