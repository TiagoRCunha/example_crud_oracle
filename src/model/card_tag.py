from model.card import Card
from model.tag import Tag

class CardTag:
    def __init__(self, 
                 card:Card=None,
                 tag:Tag=None,
                 ):
        self.set_tag(tag)
        self.set_card(card)

    def set_tag(self, tag:Tag):
        self.tag = tag

    def set_card(self, card:Card):
        self.card = card

    def get_tag(self) -> Tag:
        return self.tag

    def get_card(self) -> Card:
        return self.card

    def to_string(self):
        return f"Tag: {self.get_tag().to_string()} \n Carta: {self.get_card().to_string()}"