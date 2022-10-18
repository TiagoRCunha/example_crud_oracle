class Tag:
    def __init__(self, 
                 id:int=None,
                 name:str=None,
                 ):
        self.id = id
        self.set_name(name)

    def set_name(self, name: str):
        self.name = name

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def to_string(self):
        return f"Id: {self.get_id()} | Nome: {self.get_name()}"