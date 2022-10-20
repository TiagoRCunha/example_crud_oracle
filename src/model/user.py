from datetime import date
from model.card import Card
from model.album import Album

class User:
    def __init__(self, 
                 username:str=None,
                 password:str=None,
                 access_type:int= None
                 ):
        self.set_username(username)
        self.set_password(password)
        self.set_access_type(access_type)

    def set_username(self, username:int):
        self.username = username

    def set_password(self, password:date):
        self.password = password

    def set_access_type(self, access_type:Card):
        self.access_type = access_type

    def get_username(self) -> int:
        return self.username

    def get_password(self) -> str:
        return self.password

    def get_access_type(self) -> int:
        return self.access_type

    def to_string(self) -> str:
        return f"Nome: {self.get_username()} | Tipo de acesso: {self.get_access_type()}"