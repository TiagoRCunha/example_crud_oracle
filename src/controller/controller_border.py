from typing import Any, Dict, List, Optional, Tuple
from conexion.oracle_queries import OracleQueries
from model.border import Border
import utils.config as config
import cx_Oracle


class BorderController:
    def __init__(self):
        pass

    def insert(self, name: str, image: str, rarity_id: int) -> Border:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(*self._generate_insert_sql(name, rarity_id, image))

    def update(
        self,
        id: int,
        name: Optional[str],
        image: Optional[str],
        change: int,
    ) -> Border:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(*self._generate_update_sql(id, name, image, change))

    def delete(self, id: int):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        try:
            oracle.write("DELETE FROM \"border\" WHERE id = :id", [id])
        except cx_Oracle.IntegrityError:
            print(config.MENU_CONFIRM_CASCATE)
            selection = input("Digite sua opção\n")
            while selection != "1" and selection != "2":
                selection = input("Opção inválida\n")
            if selection == "1":
                print()
                #Delete Cascade

    def _generate_insert_sql(
        self, name: str, rarity_id: int, image: Optional[str]
    ) -> Tuple[str, List[Any]]:
        sql_insert = 'INSERT INTO "border" '
        columns = ['"name"']
        parameters: Dict[str, Any] = {":name": name}

        if image is not None:
            columns.append('"image"')
            parameters[":image"] = image

        columns.append("rarity_id")
        parameters[":rarity_id"] = rarity_id

        sql_insert += f"({', '.join(columns)}) "
        sql_insert += f"VALUES ({', '.join(parameters.keys())})"

        return sql_insert, list(parameters.values())

    def _generate_update_sql(
        self,
        id: int,
        name: Optional[str],
        image: Optional[str],
        change: int,
    ) -> Tuple[str, List[Any]]:
        sql_update = 'UPDATE "border" SET '
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
