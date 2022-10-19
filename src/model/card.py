
from model.album import Album
from model.background import Background
from model.border import Border
from model.rarity import Rarity

class Card:
    def __init__(self,
                 id:int=None,
                 number:int=None, 
                 name:str=None,
                 image:str=None,
                 background:Background=None,
                 border:Border=None,
                 rarity:Rarity=None,
                 album:Album=None
                ):
        self.id = id
        self.set_number(number)
        self.set_name(name)
        self.set_image(image)
        self.set_background(background)
        self.set_border(border)
        self.set_rarity(rarity)
        self.set_album(album)

    def set_number(self, number:int):
        self.number = number

    def set_name(self, name:str):
        self.name = name
    
    def set_image(self, image:str):
        self.image = image
    
    def set_background(self, background:Background):
        self.background = background
       
    def set_border(self, border:Border):
        self.border = border
    
    def set_rarity(self, rarity:Rarity):
        self.rarity = rarity

    def set_album(self, album:Album):
        self.album = album
    
    def get_id(self) -> int:
        return self.id
    
    def get_number(self) -> int:
        return self.number

    def get_name(self) -> str:
        return self.name
    
    def get_image(self) -> str:
        return self.image
    
    def get_background(self) -> Background:
        return self.background
     
    def get_border(self) -> Border:
        return self.border
  
    def get_rarity(self) -> Rarity:
        return self.rarity
    
    def get_album(self) -> Album:
        return self.album
 
    def to_string(self) -> str:
        text = f"id: {self.get_id()} | Número: {self.get_number()} "
        text += f"\n| Nome: {self.get_name()} | Imagem: {self.get_image()} "
        text += f"\n| Borda: {self.get_border().to_string()} \n| Fundo: {self.get_background().to_string()} "
        text += f"\n| Raridade: {self.get_rarity().to_string()} \n| Album: {self.get_album().to_string()}"
        return text