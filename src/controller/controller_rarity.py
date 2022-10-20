from typing import Any, List, Optional, Tuple
from conexion.oracle_queries import OracleQueries
from model.rarity import Rarity
from reports.relatorios import Relatorio


class RarityController:
    def __init__(self):
        pass

    def list_table(self):
        Relatorio().get_admin_rarity_select()

    def get_by_id(self, rarity_id: int) -> Optional[Rarity]:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        sql_select = 'SELECT id, "name", "tier" FROM "rarity" WHERE id = :id'
        df_rarity = oracle.sqlToDataFrame(sql_select, [rarity_id])

        if df_rarity.empty:
            return None

        return Rarity(
            df_rarity.id.values[0],
            df_rarity.name.values[0],
            df_rarity.rarity.values[0],
        )

    def insert(self, name: str, tier: int) -> Rarity:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        sql_insert = 'INSERT INTO "rarity" ("name", "tier") VALUES (:name, :tier)'
        oracle.write(sql_insert, [name, tier])

        sql_select = 'SELECT id, "name", "tier" FROM "rarity" WHERE "name" = :name'
        df_rarity = oracle.sqlToDataFrame(sql_select, [name])

        return Rarity(
            df_rarity.id.values[0],
            df_rarity.name.values[0],
            df_rarity.rarity.values[0],
        )

    def update(
        self, rarity_id: int, name: Optional[str], tier: Optional[int]
    ) -> Rarity:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(*self._generate_update_sql(rarity_id, name, tier))

        sql_select = 'SELECT id, "name", "tier" FROM "rarity" WHERE "name" = :name'
        df_rarity = oracle.sqlToDataFrame(sql_select, [name])

        return Rarity(
            df_rarity.id.values[0],
            df_rarity.name.values[0],
            df_rarity.rarity.values[0],
        )

    def delete(self, rarity_id: int):
        oracle = OracleQueries()
        oracle.connect()
        oracle.write('DELETE FROM "rarity" WHERE id = :id', [rarity_id])

    def name_exists(self, oracle: OracleQueries, name: str) -> bool:
        sql = 'SELECT "name" FROM "rarity" WHERE "name" = :name'
        df_cliente = oracle.sqlToDataFrame(sql, [name])
        return not df_cliente.empty

    def _generate_update_sql(
        self,
        id: int,
        name: Optional[str],
        tier: Optional[int],
    ) -> Tuple[str, List[Any]]:
        sql_update = 'UPDATE "rarity" SET '
        set_list = []
        parameters = []

        if name is not None:
            set_list.append('"name" = :name')
            parameters.append(name)

        if tier is not None:
            set_list.append('"tier" = :tier')
            parameters.append(tier)

        sql_update += ", ".join(set_list) + " "
        sql_update += "WHERE id = :id"
        parameters.append(id)

        return sql_update, parameters
