from model.border import Border
from model.tag import Tag

class BorderTag:
    def __init__(self, 
                 border:Border=None,
                 tag:Tag=None,
                 ):
        self.set_tag(tag)
        self.set_border(border)

    def set_tag(self, tag:Tag):
        self.tag = tag

    def set_border(self, border:Border):
        self.border = border

    def get_tag(self) -> Tag:
        return self.tag

    def get_border(self) -> Border:
        return self.border

    def to_string(self):
        return f"Tag: {self.get_tag().to_string()} \n Borda: {self.get_border().to_string()}"