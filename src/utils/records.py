from conexion.oracle_queries import OracleQueries

class Records:

    def __init__(self):
        self.created_by = "Henrique Klayton, Tiago Rodrigues e Victor Binda"
        self.oracle = OracleQueries()

    def select_admin_album_view(self):
        self.oracle.connect()
        return self.oracle.sqlToDataFrame("select * from admin_album_view")
    
    def select_admin_card_view(self):
        self.oracle.connect()
        return self.oracle.sqlToDataFrame("select * from admin_card_view")

    def select_admin_users_view(self):
        self.oracle.connect()
        return self.oracle.sqlToDataFrame("select * from admin_users_view")
    
    def total_albuns(self) -> int:
        oracle = OracleQueries()
        oracle.connect()
        return int(oracle.sqlToDataFrame("select count(*) from labdatabase.\"album\"").iloc[0])

    def list_albuns(self):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame("select title from labdatabase.\"album\""))

    def show_album(self, id):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame(f"select title, \"description\" from labdatabase.\"album\" where id = '{id}'"))

    def total_users(self) -> int:
        oracle = OracleQueries()
        oracle.connect()
        return int(oracle.sqlToDataFrame("select count(*) from labdatabase.\"user\"").iloc[0])

    def list_users(self):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame("select username from labdatabase.\"user\""))

    def show_user(self, id):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame(f"select username, \"password\", access_type from labdatabase.\"user\" where id = '{id}'"))

    def total_cards(self) -> int:
        oracle = OracleQueries()
        oracle.connect()
        return int(oracle.sqlToDataFrame("select count(*) from labdatabase.\"card\"").iloc[0])

    def list_cards(self):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame("select \"name\" from labdatabase.\"card\""))

    def show_card(self, id):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame(f"select \"image\", \"name\" from labdatabase.\"card\" where id = '{id}'"))

    def total_tags(self) -> int:
        oracle = OracleQueries()
        oracle.connect()
        return int(oracle.sqlToDataFrame("select count(*) from labdatabase.\"tag\"").iloc[0])

    def list_tags(self):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame("select \"name\" from labdatabase.\"tag\""))

    def show_tag(self, id):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame(f"select \"name\" from labdatabase.\"tag\" where id = '{id}'"))

    def total_backgrounds(self) -> int:
        oracle = OracleQueries()
        oracle.connect()
        return int(oracle.sqlToDataFrame("select count(*) from labdatabase.\"background\"").iloc[0])

    def list_background(self):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame("select \"name\", rarity_id from labdatabase.\"background\""))

    def show_background(self, id):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame(f"select \"image\", \"name\", rarity_id from labdatabase.\"background\" where id = '{id}'"))

    def total_borders(self) -> int:
        oracle = OracleQueries()
        oracle.connect()
        return int(oracle.sqlToDataFrame("select count(*) from labdatabase.\"border\"").iloc[0])

    def list_borders(self):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame("select \"name\", rarity_id from labdatabase.\"border\""))

    def show_border(self, id):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame(f"select \"image\", \"name\", rarity_id from labdatabase.\"border\" where id = '{id}'"))

    def total_rarity(self) -> int:
        oracle = OracleQueries()
        oracle.connect()
        return int(oracle.sqlToDataFrame("select count(*) from labdatabase.\"rarity\"").iloc[0])

    def list_rarity(self):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame("select \"name\", \"tier\" from labdatabase.\"rarity\""))

    def show_rarity(self, id):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame(f"select \"name\", \"tier\" from labdatabase.\"rarity\" where id = '{id}'"))

    def total_border_tag(self) -> int:
        oracle = OracleQueries()
        oracle.connect()
        return int(oracle.sqlToDataFrame("select count(*) from labdatabase.\"border_tag\"").iloc[0])

    def list_border_tag(self):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame("select border_id, tag_id from labdatabase.\"border_tag\""))

    def show_border_tag(self, border_id, tag_id):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame(f"select border_id, tag_id from labdatabase.\"border_tag\" where border_id = '{border_id}' and tag_id = '{tag_id}'"))

    def total_card_tag(self) -> int:
        oracle = OracleQueries()
        oracle.connect()
        return int(oracle.sqlToDataFrame("select count(*) from labdatabase.\"card_tag\"").iloc[0])

    def list_card_tag(self):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame("select card_id, tag_id from labdatabase.\"card_tag\""))

    def show_card_tag(self, card_id, tag_id):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame(f"select card_id, tag_id from labdatabase.\"card_tag\" where card_id = '{card_id}' and tag_id = '{tag_id}"))

    def total_background_tag(self) -> int:
        oracle = OracleQueries()
        oracle.connect()
        return int(oracle.sqlToDataFrame("select count(*) from labdatabase.\"background_tag\"").iloc[0])

    def list_background_tag(self):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame("select background_id, tag_id from labdatabase.\"background_tag\""))

    def show_background_tag(self, background_id, tag_id):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame(f"select background_id, tag_id from labdatabase.\"background_tag\" where card_id = '{background_id}' and tag_id = '{tag_id}"))

    def total_user_card(self) -> int:
        oracle = OracleQueries()
        oracle.connect()
        return int(oracle.sqlToDataFrame("select count(*) from labdatabase.\"user_card\"").iloc[0])

    def list_user_card(self):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame("select user_id, card_id from labdatabase.\"user_card\""))

    def show_user_card(self, user_id, card_id):
        oracle = OracleQueries()
        oracle.connect()
        return(oracle.sqlToDataFrame(f"select user_id, card_id from labdatabase.\"user_card\" where card_id = '{user_id}' and tag_id = '{card_id}"))


    def get_init(self):
        return f"""
    Bem vindo ao Album Digital
Desenvolvedores: {self.created_by}
   
====== Total de Registro no Banco ======
Usuários: {self.total_users()}
Albuns: {self.total_albuns()}
Cartas: {self.total_cards()}
Tags: {self.total_tags()}
Background: {self.total_backgrounds()}
Bordas: {self.total_borders()}
Raridades: {self.total_rarity()}
========================================
"""
