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
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 5, 'ronaldinho.png', 'Ronaldinho Gaucho', :1, :2, :3, :4)", [int(background_legendary_id.iloc[0]["id"]), int(border_legendary_id.iloc[0]["id"]), int(rarity_legendary_id.iloc[0]["id"]), int(album_copa_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 6, 'ibrahimovic.png', 'Zlatan Ibrahimović', :1, :2, :3, :4)", [int(background_epic_id.iloc[0]["id"]), int(border_epic_id.iloc[0]["id"]), int(rarity_epic_id.iloc[0]["id"]), int(album_copa_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 7, 'zidane.png', 'Zinédine Zidane', :1, :2, :3, :4)", [int(background_common_id.iloc[0]["id"]), int(border_common_id.iloc[0]["id"]), int(rarity_common_id.iloc[0]["id"]), int(album_copa_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 8, 'kaka.png', 'Kaka', :1, :2, :3, :4)", [int(background_common_id.iloc[0]["id"]), int(border_common_id.iloc[0]["id"]), int(rarity_common_id.iloc[0]["id"]), int(album_copa_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 9, 'pele.png', 'Pele', :1, :2, :3, :4)", [int(background_rare_id.iloc[0]["id"]), int(border_rare_id.iloc[0]["id"]), int(rarity_rare_id.iloc[0]["id"]), int(album_copa_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 10, 'maradona.png', 'Diego Maradona', :1, :2, :3, :4)", [int(background_uncommon_id.iloc[0]["id"]), int(border_uncommon_id.iloc[0]["id"]), int(rarity_uncommon_id.iloc[0]["id"]), int(album_copa_id.iloc[0]["id"])])

oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 4, 'squirtle.png', 'Squirtle', :1, :2, :3, :4)", [int(background_common_id.iloc[0]["id"]), int(border_common_id.iloc[0]["id"]), int(rarity_common_id.iloc[0]["id"]), int(album_pokemon_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 5, 'pidgey.png', 'Pidgey', :1, :2, :3, :4)", [int(background_uncommon_id.iloc[0]["id"]), int(border_uncommon_id.iloc[0]["id"]), int(rarity_uncommon_id.iloc[0]["id"]), int(album_pokemon_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 6, 'psyduck.png', 'Psyduck', :1, :2, :3, :4)", [int(background_rare_id.iloc[0]["id"]), int(border_rare_id.iloc[0]["id"]), int(rarity_rare_id.iloc[0]["id"]), int(album_pokemon_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 7, 'onix.png', 'Onix', :1, :2, :3, :4)", [int(background_common_id.iloc[0]["id"]), int(border_common_id.iloc[0]["id"]), int(rarity_common_id.iloc[0]["id"]), int(album_pokemon_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 8, 'eevee.png', 'Eevee', :1, :2, :3, :4)", [int(background_rare_id.iloc[0]["id"]), int(border_rare_id.iloc[0]["id"]), int(rarity_rare_id.iloc[0]["id"]), int(album_pokemon_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 9, 'dratini.png', 'Dratini', :1, :2, :3, :4)", [int(background_common_id.iloc[0]["id"]), int(border_common_id.iloc[0]["id"]), int(rarity_common_id.iloc[0]["id"]), int(album_pokemon_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 10, 'articuno.png', 'Articuno', :1, :2, :3, :4)", [int(background_legendary_id.iloc[0]["id"]), int(border_legendary_id.iloc[0]["id"]), int(rarity_legendary_id.iloc[0]["id"]), int(album_pokemon_id.iloc[0]["id"])])

oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 4, 'hagrid.png', 'Rúbeo Hadrid', :1, :2, :3, :4)", [int(background_uncommon_id.iloc[0]["id"]), int(border_uncommon_id.iloc[0]["id"]), int(rarity_uncommon_id.iloc[0]["id"]), int(album_harrypotter_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 5, 'dumbledore.png', 'Albus Dumbledore', :1, :2, :3, :4)", [int(background_legendary_id.iloc[0]["id"]), int(border_legendary_id.iloc[0]["id"]), int(rarity_legendary_id.iloc[0]["id"]), int(album_harrypotter_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 6, 'voldemort.png', 'Lord Voldemort', :1, :2, :3, :4)", [int(background_epic_id.iloc[0]["id"]), int(border_epic_id.iloc[0]["id"]), int(rarity_epic_id.iloc[0]["id"]), int(album_harrypotter_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 7, 'snape.png', 'Severus Snape', :1, :2, :3, :4)", [int(background_rare_id.iloc[0]["id"]), int(border_rare_id.iloc[0]["id"]), int(rarity_rare_id.iloc[0]["id"]), int(album_harrypotter_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 8, 'luna.png', 'Luna Lovegood', :1, :2, :3, :4)", [int(background_common_id.iloc[0]["id"]), int(border_common_id.iloc[0]["id"]), int(rarity_common_id.iloc[0]["id"]), int(album_harrypotter_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 9, 'dobby.png', 'Dobby', :1, :2, :3, :4)", [int(background_common_id.iloc[0]["id"]), int(border_common_id.iloc[0]["id"]), int(rarity_common_id.iloc[0]["id"]), int(album_harrypotter_id.iloc[0]["id"])])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 10, 'sirius.png', 'Sirius Black', :1, :2, :3, :4)", [int(background_common_id.iloc[0]["id"]), int(border_common_id.iloc[0]["id"]), int(rarity_common_id.iloc[0]["id"]), int(album_harrypotter_id.iloc[0]["id"])])
