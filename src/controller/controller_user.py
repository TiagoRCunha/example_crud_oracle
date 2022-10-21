from typing import Any, Dict, List, Optional, Tuple
from conexion.oracle_queries import OracleQueries
from model.user import User
from reports.relatorios import Relatorio


class UserController:
    def __init__(self):
        pass

    def list_table(self):
        Relatorio().get_admin_users_view()

    def get_by_id(self, user_id: int) -> Optional[User]:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        sql_select = 'SELECT id, username, password, access_type, album_id FROM "user" WHERE id = :id'
        df_rarity = oracle.sqlToDataFrame(sql_select, [user_id])

        if df_rarity.empty:
            return None

        return User(
            df_rarity.id.values[0],
            df_rarity.username.values[0],
            df_rarity.password.values[0],
            df_rarity.access_type.values[0],
            df_rarity.album_id.values[0],
        )

    def insert(
        self, name: str, password: str, access_type: str, album_id: Optional[int] = None
    ):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(*self._generate_insert_sql(name, password, access_type, album_id))

    def update(
        self,
        user_id: int,
        name: Optional[str] = None,
        password: Optional[str] = None,
        access_type: Optional[str] = None,
        album_id: Optional[int] = None,
    ):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        oracle.write(
            *self._generate_update_sql(
                user_id,
                name,
                password,
                access_type,
                album_id,
            )
        )

    def delete(self, user_id: int):
        oracle = OracleQueries()
        oracle.connect()
        oracle.write('DELETE FROM "user" WHERE id = :id', [user_id])

    def _generate_insert_sql(
        self, name: str, password: str, access_type: str, album_id: Optional[int]
    ) -> Tuple[str, List[Any]]:
        sql_insert = 'INSERT INTO "user" '
        columns = ["username", '"password"', "access_type"]
        parameters: Dict[str, Any] = {
            ":name": name,
            ":password": password,
            ":access_type": access_type,
        }

        if album_id is not None:
            columns.append("album_id")
            parameters[":album_id"] = album_id

        sql_insert += f"({', '.join(columns)}) "
        sql_insert += f"VALUES ({', '.join(parameters.keys())})"

        return sql_insert, list(parameters.values())

    def _generate_update_sql(
        self,
        user_id: int,
        name: Optional[str],
        password: Optional[str],
        access_type: Optional[str],
        album_id: Optional[int],
    ) -> Tuple[str, List[Any]]:
        sql_update = 'UPDATE "border" SET '
        set_list = []
        parameters = []

        if name is not None:
            set_list.append("username = :name")
            parameters.append(name)

        if password is not None:
            set_list.append('"password" = :password')
            parameters.append(password)

        if access_type is not None:
            set_list.append("access_type = :access_type")
            parameters.append(access_type)

        if album_id is not None:
            set_list.append("album_id = :album_id")
            parameters.append(album_id)

        sql_update += ", ".join(set_list) + " "
        sql_update += "WHERE id = :id"
        parameters.append(user_id)

        return sql_update, parameters
