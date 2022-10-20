from conexion.oracle_queries import OracleQueries
class Album:
    def __init__(self, 
                 id:int=None,
                 title:str=None,
                 card_count:int=None, 
                 page_number:int=None,
                 description:str=None
                 ):
        self.id = id
        self.set_title(title)
        self.set_card_count(card_count)
        self.set_page_number(page_number)
        self.set_description(description)
        with open("./sql/insert_card.sql") as f:
            self.query_insert_card = f.read()

    def set_title(self, title:str):
        self.title = title

    def set_card_count(self, card_count:int):
        self.card_count = card_count

    def set_page_number(self, page_number:int):
        self.page_number = page_number

    def set_description(self, description:str):
        self.description = description
    
    def get_id(self) -> int:
        return self.id

    def get_title(self) -> str:
        return self.title

    def get_card_count(self) -> int:
        return self.card_count

    def get_page_number(self) -> int:
        return self.page_number

    def get_description(self) -> str:
        return self.description

    def to_string(self) -> str:
        return f"título: {self.get_title()} | Número de cartas: {self.get_card_count()} | Número de páginas: {self.get_page_number()} | \nDescrição: {self.get_description()}\n"
    
    def persist(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        return oracle.write(self.query_insert_card, [self.title, self.card_count, self.page_number, self.description])