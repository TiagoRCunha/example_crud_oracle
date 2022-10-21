from typing import Any, Dict, List, Optional, Tuple
from conexion.oracle_queries import OracleQueries
from model.card import Card
import utils.config as config
import cx_Oracle


class CardController:
    def __init__(self):
        pass

    def insert(self, number: str, image: str, name: str, background: str, border: str, rarity: str, album: str) -> Card:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(*self._generate_insert_sql(number, image, name, background, border, rarity, album))

    def update(
        self,
        id: int,
        image: Optional[str],
        name: Optional[str],
        change: int,
    ) -> Card:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(*self._generate_update_sql(id, image, name, change))

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
        self,  number: str, image: str, name: str, background: str, border: str, rarity: str, album: str
    ) -> Tuple[str, List[Any]]:
        sql_insert = 'INSERT INTO "card" '
        columns = ['"number"']
        parameters: Dict[str, Any] = {":numy": number}
        
        columns.append('"image"')
        parameters[":image"] = image

        columns.append('"name"')
        parameters[":name"] = name

        columns.append('background_id')
        parameters[":background"] = background

        columns.append('border_id')
        parameters[":border"] = border
        
        columns.append('rarity_id')
        parameters[":rarity"] = rarity
        
        columns.append('album_id')
        parameters[":album"] = album
        
        
        sql_insert += f"({', '.join(columns)}) "
        sql_insert += f"VALUES ({', '.join(parameters.keys())})"

        return sql_insert, list(parameters.values())

    def _generate_update_sql(
        self,
        id: int,
        image: Optional[str],
        name: Optional[str],
        change: int,
    ) -> Tuple[str, List[Any]]:
        sql_update = 'UPDATE "album" SET '
        set_list = []
        parameters = []

        if change == 1:
            if image is not None:
                set_list.append('"image" = :image')
                parameters.append(image)

        if change == 2:
            if name is not None:
                set_list.append('"name" = :name')
                parameters.append(name)

        sql_update += ", ".join(set_list) + " "
        sql_update += "WHERE id = :id"
        parameters.append(id)

        return sql_update, parameters
