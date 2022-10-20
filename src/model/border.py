from typing import Optional
from model.rarity import Rarity


class Border:
    def __init__(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None,
        image: Optional[str] = None,
        rarity: Optional[Rarity] = None,
    ):
        self.id = id or 0
        self.set_name(name or "")
        self.set_image(image or "")
        self.set_rarity(rarity or Rarity())

    def set_name(self, name: str):
        self.name = name

    def set_image(self, image: str):
        self.image = image

    def set_rarity(self, rarity: Rarity):
        self.rarity = rarity

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_image(self) -> str:
        return self.image

    def get_rarity(self) -> Rarity:
        return self.rarity

    def to_string(self) -> str:
        return f"Id: {self.get_id()} | Nome: {self.get_name()} | Imagem: {self.get_image()}\n| Raridade: {self.get_rarity().to_string()}"
