from typing import Optional
from conexion.oracle_queries import OracleQueries
from model.tag import Tag
from reports.relatorios import Relatorio


class TagController:
    def __init__(self):
        pass

    def list_table(self):
        Relatorio().get_admin_tag_select()

    def get_by_id(self, tag_id: int) -> Optional[Tag]:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        sql_select = 'SELECT id, "name" FROM "tag" WHERE "id" = :id'
        df_tag = oracle.sqlToDataFrame(sql_select, [tag_id])

        if df_tag.empty:
            return None

        return Tag(df_tag.id.values[0], df_tag.name.values[0])

    def insert(self, name: str) -> Optional[Tag]:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write('INSERT INTO "tag" ("name") VALUES (:name)', [name])

        sql_select = 'SELECT id, "name" FROM "tag" WHERE "name" = :name'
        df_tag = oracle.sqlToDataFrame(sql_select, [name])
        return Tag(df_tag.id.values[0], df_tag.name.values[0])

    def update(self, tag_id: int, name: str):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        sql_update = 'UPDATE "tag" SET "name" = :name WHERE id = :id'
        oracle.write(sql_update, [name, tag_id])

        sql_select = 'SELECT id, "name" FROM "tag" WHERE "name" = :name'
        df_tag = oracle.sqlToDataFrame(sql_select, [name])

        return Tag(df_tag.id.values[0], df_tag.name.values[0])

    def delete(self, tag_id: int):
        oracle = OracleQueries()
        oracle.connect()
        oracle.write("DELETE FROM tag WHERE id = :id", [tag_id])

    def name_exists(self, oracle: OracleQueries, name: str) -> bool:
        sql = 'SELECT "name" FROM "tag" WHERE "name" = :name'
        df_cliente = oracle.sqlToDataFrame(sql, [name])
        return not df_cliente.empty
