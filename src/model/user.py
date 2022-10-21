from datetime import date
from typing import Optional
from model.card import Card
from model.album import Album


class User:
    def __init__(
        self,
        id: Optional[int] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        access_type: Optional[int] = None,
    ):
        self.set_id(id)
        self.set_username(username)
        self.set_password(password)
        self.set_access_type(access_type)

    def set_id(self, id: int):
        self.id = id

    def set_username(self, username: str):
        self.username = username

    def set_password(self, password: date):
        self.password = password

    def set_access_type(self, access_type: Card):
        self.access_type = access_type

    def get_id(self) -> int:
        return self.id

    def get_username(self) -> str:
        return self.username

    def get_password(self) -> str:
        return self.password

    def get_access_type(self) -> int:
        return self.access_type

    def to_string(self) -> str:
        return f"Id: {self.get_id()} | Nome: {self.get_username()} | Tipo de acesso: {self.get_access_type()}"
