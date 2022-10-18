from model.card import Card
from model.user import User

class UserCard:
    def __init__(self, 
                 card:Card=None,
                 user:User=None,
                 ):
        self.set_card(card)
        self.set_user(user)

    def set_card(self, card:Card):
        self.card = card

    def set_user(self, user:User):
        self.user = user

    def get_card(self) -> Card:
        return self.card

    def get_user(self) -> User:
        return self.user

    def to_string(self):
        return f"Carta: {self.get_card().to_string()} \n Usuário: {self.get_user()}"