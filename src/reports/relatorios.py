from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        with open("./views/user_available_cards_select.sql") as f:
            self.query_user_cards_available = f.read()
        with open("./views/user_list_own_card_select.sql") as f:
            self.query_user_list_own_card_select = f.read()

        self.txt = "Pressione Enter para sair"

    def get_admin_album_view(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame("SELECT * FROM admin_album_view"))
        input(self.txt)

    def get_admin_card_view(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame("SELECT * FROM admin_card_view"))
        input(self.txt)

    def get_admin_users_view(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame("SELECT * FROM admin_users_view"))
        input(self.txt)

    def get_user_cards_available(self, user_id: int):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_user_cards_available, [user_id]))
        input(self.txt)

    def get_user_list_own_card_select(self, user_id: int):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_user_list_own_card_select, [user_id]))
        input(self.txt)