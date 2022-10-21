from typing import Optional

from pandas import DataFrame
from conexion.oracle_queries import OracleQueries
from controller.controller_rarity import RarityController
from model.background import Background

class BackgroundController:
    def __init__(self):
        self.oracle = OracleQueries(can_write=True)
        self.oracle.connect()

    def list_table(self) -> DataFrame:
        return self.oracle.sqlToDataFrame('SELECT id, "name" from "background"')

    def get_by_id(self, background_id: int) -> Optional[Background]:
        sql_select = 'SELECT id, "name", "image", rarity_id FROM "background" WHERE id = :id'
        df_background = self.oracle.sqlToDataFrame(sql_select, [background_id])

        if df_background.empty:
            return None
        
        background = Background(df_background.id.values[0], df_background.name.values[0], df_background.image.values[0])
        
        if df_background.rarity_id.values[0]:
            background.set_rarity(RarityController().get_by_id(int(df_background.rarity_id.values[0])))
        return background

    def insert(self, name: str, image: str, rarity_id: int = None) -> Optional[Background]:
        self.oracle.write('INSERT INTO "background" ("name", "image", rarity_id) VALUES (:name, :image, :rarity_id)', [name, image, rarity_id])

        sql_select = 'SELECT id, "name", "image", rarity_id FROM "background" WHERE "name" = :name'
        df_background = self.oracle.sqlToDataFrame(sql_select, [name])
        return Background(df_background.id.values[0], df_background.name.values[0], df_background.image.values[0])

    def update(self, background_id: int, name: str = None, image: str = None, rarity_id: int = None):
        if name:
            sql_update = 'UPDATE "background" SET "name" = :name WHERE id = :id'
            self.oracle.write(sql_update, [name, background_id])
        if image:
            sql_update = 'UPDATE "background" SET "image" = :image WHERE id = :id'
            self.oracle.write(sql_update, [image, background_id])
        if rarity_id:
            sql_update = 'UPDATE "background" SET rarity_id = :rarity_id WHERE id = :id'
            self.oracle.write(sql_update, [rarity_id, background_id])
            
        sql_select = 'SELECT id, "name", "image", rarity_id FROM "background" WHERE id = :id'
        df_background = self.oracle.sqlToDataFrame(sql_select, [background_id])
        new_background = Background(df_background.id.values[0], df_background.name.values[0], df_background.image.values[0])
        if rarity_id:
            rarity=RarityController().get_by_id(rarity_id)
            new_background.set_rarity(rarity)
        return new_background

    def delete(self, background_id: int):
        self.oracle.write("DELETE FROM background WHERE id = :id", [background_id])

    def name_exists(self, oracle: OracleQueries, name: str) -> bool:
        sql = 'SELECT "name" FROM "background" WHERE "name" = :name'
        df_cliente = oracle.sqlToDataFrame(sql, [name])
        return not df_cliente.empty
