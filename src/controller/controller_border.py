from typing import Any, Dict, List, Optional, Tuple
from conexion.oracle_queries import OracleQueries
from controller.controller_rarity import RarityController
from model.border import Border
from reports.reports import Relatorio


class BorderController:
    def __init__(self):
        pass

    def list_table(self):
        Relatorio().get_admin_border_select()

    def get_by_id(self, border_id: int) -> Optional[Border]:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        sql_select = 'SELECT id, "name" "image" from "border" WHERE "id" = :id'
        df_border = oracle.sqlToDataFrame(sql_select, [border_id])

        if df_border.empty:
            return None

        return Border(
            df_border.id.values[0],
            df_border.name.values[0],
            df_border.image.values[0],
        )

    def insert(self, name: str, image: str, rarity_id: int) -> Border:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(*self._generate_insert_sql(name, rarity_id, image))

        sql_select = 'SELECT id, "name" "image" from "border" WHERE "name" = :name'
        df_border = oracle.sqlToDataFrame(sql_select, [name])

        rarity_id_select: Any = df_border.rarity_id.values[0]
        rarity = RarityController().get_by_id(rarity_id_select)

        return Border(
            df_border.id.values[0],
            df_border.name.values[0],
            df_border.image.values[0],
            rarity,
        )

    def update(
        self,
        id: int,
        name: Optional[str],
        image: Optional[str],
        rarity_id: Optional[int],
    ) -> Border:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(*self._generate_update_sql(id, name, image, rarity_id))

        sql_select = 'SELECT id, "name", "image" from "border" WHERE "name" = :name'
        df_border = oracle.sqlToDataFrame(sql_select, [name])

        rarity_id_select: Any = df_border.rarity_id.values[0]
        rarity = RarityController().get_by_id(rarity_id_select)

        return Border(
            df_border.id.values[0],
            df_border.name.values[0],
            df_border.image.values[0],
            rarity,
        )

    def delete(self, rarity_id: int):
        oracle = OracleQueries()
        oracle.connect()
        oracle.write("DELETE FROM border WHERE id = :id", [rarity_id])

    def name_exists(self, oracle: OracleQueries, name: str) -> bool:
        sql = 'SELECT "name" FROM "border" WHERE "name" = :name'
        df_cliente = oracle.sqlToDataFrame(sql, [name])
        return not df_cliente.empty

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
        rarity_id: Optional[int],
    ) -> Tuple[str, List[Any]]:
        sql_update = 'UPDATE "border" SET '
        set_list = []
        parameters = []

        if name is not None:
            set_list.append('"name" = :name')
            parameters.append(name)

        if image is not None:
            set_list.append('"image" = :image')
            parameters.append(image)

        if rarity_id is not None:
            set_list.append("rarity_id = :rarity_id")
            parameters.append(rarity_id)

        sql_update += ", ".join(set_list) + " "
        sql_update += "WHERE id = :id"
        parameters.append(id)

        return sql_update, parameters
