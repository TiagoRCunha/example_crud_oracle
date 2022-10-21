from typing import Any, Dict, List, Optional, Tuple
from conexion.oracle_queries import OracleQueries
from model.album import Album
import utils.config as config
import cx_Oracle


class AlbumController:
    def __init__(self):
        pass

    def insert(self, title: str, card_count: str, page_number: str, description: str) -> Album:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(*self._generate_insert_sql(title, card_count, page_number, description))

    def update(
        self,
        id: int,
        title: Optional[str],
        description: Optional[str],
        change: int,
    ) -> Album:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(*self._generate_update_sql(id, title, description, change))

    def delete(self, id: int):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        try:
            oracle.write("DELETE FROM \"album\" WHERE id = :id", [id])
        except cx_Oracle.IntegrityError:
            print(config.MENU_CONFIRM_CASCATE)
            selection = input("Digite sua opção\n")
            while selection != "1" and selection != "2":
                selection = input("Opção inválida\n")
            if selection == "1":
                print()
                #Delete Cascade

    def _generate_insert_sql(
        self,  title: str, card_count: str, page_number: str, description: str
    ) -> Tuple[str, List[Any]]:
        sql_insert = 'INSERT INTO "album" '
        columns = ["title"]
        parameters: Dict[str, Any] = {":title": title}

        
        columns.append("card_count")
        parameters[":card_count"] = card_count

        columns.append("page_number")
        parameters[":page_number"] = page_number

        columns.append('"description"')
        parameters[":description"] = description

        sql_insert += f"({', '.join(columns)}) "
        sql_insert += f"VALUES ({', '.join(parameters.keys())})"

        return sql_insert, list(parameters.values())

    def _generate_update_sql(
        self,
        id: int,
        title: Optional[str],
        description: Optional[str],
        change: int,
    ) -> Tuple[str, List[Any]]:
        sql_update = 'UPDATE "album" SET '
        set_list = []
        parameters = []

        if change == 1:
            if title is not None:
                set_list.append('title = :title')
                parameters.append(title)

        if change == 2:
            if description is not None:
                set_list.append('"description" = :description')
                parameters.append(description)

        sql_update += ", ".join(set_list) + " "
        sql_update += "WHERE id = :id"
        parameters.append(id)

        return sql_update, parameters
