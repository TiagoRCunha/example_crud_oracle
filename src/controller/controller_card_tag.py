from typing import Any, Dict, List, Optional, Tuple
from conexion.oracle_queries import OracleQueries
from model.card_tag import CardTag
import utils.config as config
import cx_Oracle


class CardTagController:
    def __init__(self):
        pass

    def insert(self, card: str, tag: str) -> CardTag:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(*self._generate_insert_sql(card, tag))

    def delete(self, id: int):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        try:
            oracle.write("DELETE FROM \"card\" WHERE id = :id", [id])
        except cx_Oracle.IntegrityError:
            print(config.MENU_CONFIRM_CASCATE)
            selection = input("Digite sua opção\n")
            while selection != "1" and selection != "2":
                selection = input("Opção inválida\n")
            if selection == "1":
                print()
                #Delete Cascade

    def _generate_insert_sql(
        self,  card: str, tag: str
    ) -> Tuple[str, List[Any]]:
        sql_insert = 'INSERT INTO "card_tag" '
        columns = ['card_id']
        parameters: Dict[str, Any] = {":card": card}
        
        columns.append('tag_id')
        parameters[":tag"] = tag        
        
        sql_insert += f"({', '.join(columns)}) "
        sql_insert += f"VALUES ({', '.join(parameters.keys())})"

        return sql_insert, list(parameters.values())