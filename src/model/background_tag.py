from model.background import Background
from model.tag import Tag

class BackgroundTag:
    def __init__(self, 
                 background:Background=None,
                 tag:Tag=None,
                 ):
        self.set_tag(tag)
        self.set_background(background)

    def set_tag(self, tag:Tag):
        self.tag = tag

    def set_background(self, background:Background):
        self.background = background

    def get_tag(self) -> Tag:
        return self.tag

    def get_background(self) -> Background:
        return self.background

    def to_string(self):
        return f"Tag: {self.get_tag().to_string()} \n Carta: {self.get_background().to_string()}"