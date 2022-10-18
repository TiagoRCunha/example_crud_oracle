class Rarity:
    def __init__(self, 
                 id:int=None,
                 name:str=None,
                 tier:int=None
                 ):
        self.id = id
        self.set_name(name)
        self.set_tier(tier)

    def set_name(self, name:str):
        self.name = name

    def set_tier(self, tier:int):
        self.tier = tier

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_tier(self) -> int:
        return self.tier

    def to_string(self) -> str:
        return f"Codigo: {self.get_id()} | Nome: {self.get_name()} | Nível: {self.get_tier()}"