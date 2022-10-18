from model.rarity import Rarity

class Background:
    def __init__(self, 
                 id:int=None,
                 name:str=None,
                 image:str=None,
                 rarity:Rarity=None
                 ):
        self.id = id
        self.set_name(name)
        self.set_image(image)
        self.set_rarity(rarity)

    def set_name(self, name:str):
        self.name = name

    def set_image(self, image:str):
        self.image = image
    
    def set_rarity(self, rarity:Rarity):
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