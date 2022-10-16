from conexion.oracle_queries import OracleQueries

oracle = OracleQueries(can_write=True)
oracle.connect()

rarity_common_id = oracle.sqlToDataFrame("select id from labdatabase.\"rarity\" where \"tier\" = '1'")
rarity_uncommon_id = oracle.sqlToDataFrame("select id from labdatabase.\"rarity\" where \"tier\" = '2'")
rarity_rare_id = oracle.sqlToDataFrame("select id from labdatabase.\"rarity\" where \"tier\" = '3'")
rarity_epic_id = oracle.sqlToDataFrame("select id from labdatabase.\"rarity\" where \"tier\" = '4'")
rarity_legendary_id = oracle.sqlToDataFrame("select id from labdatabase.\"rarity\" where \"tier\" = '5'")

album_copa_id = oracle.sqlToDataFrame("select id from labdatabase.\"album\" where \"title\" = 'Copa do Mundo 2022'")
album_harrypotter_id = oracle.sqlToDataFrame("select id from labdatabase.\"album\" where \"title\" = 'Harry Potter'")
album_pokemon_id = oracle.sqlToDataFrame("select id from labdatabase.\"album\" where \"title\" = 'Pokemon'")

background_common_id = oracle.sqlToDataFrame("select id from labdatabase.\"background\" where \"rarity_id\" = '1'")
background_uncommon_id = oracle.sqlToDataFrame("select id from labdatabase.\"background\" where \"rarity_id\" = '2'")
background_rare_id = oracle.sqlToDataFrame("select id from labdatabase.\"background\" where \"rarity_id\" = '3'")
background_epic_id = oracle.sqlToDataFrame("select id from labdatabase.\"background\" where \"rarity_id\" = '4'")
background_legendary_id = oracle.sqlToDataFrame("select id from labdatabase.\"background\" where \"rarity_id\" = '5'")

border_common_id = oracle.sqlToDataFrame("select id from labdatabase.\"border\" where \"rarity_id\" = '1'")
border_uncommon_id = oracle.sqlToDataFrame("select id from labdatabase.\"border\" where \"rarity_id\" = '2'")
border_rare_id = oracle.sqlToDataFrame("select id from labdatabase.\"border\" where \"rarity_id\" = '3'")
border_epic_id = oracle.sqlToDataFrame("select id from labdatabase.\"border\" where \"rarity_id\" = '4'")
border_legendary_id = oracle.sqlToDataFrame("select id from labdatabase.\"border\" where \"rarity_id\" = '5'")

oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 4, 'mbappe.png', 'Kylian Mbappe', :1, :2, :3, :4)", [int(background_uncommon_id.iloc[0]["id"]), int(border_uncommon_id.iloc[0]["id"]), int(rarity_uncommon_id.iloc[0]["id"]), int(album_copa_id.iloc[0]["id"])])