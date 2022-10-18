from conexion.oracle_queries import OracleQueries

oracle = OracleQueries(can_write=True)
oracle.connect()

count = 1

rarity_list = ["commom", "uncommon", "rare", "epic", "legendary"] # 0 = common, 1 = uncommon, 2 = rare, 3 = epic, 4 = legendary
for x in range(len(rarity_list)):
    rarity_list[x] = int(oracle.sqlToDataFrame(f"select id from labdatabase.\"rarity\" where \"tier\" = '{x + 1}'").iloc[0]["id"])
    count += 1
    if count>len(rarity_list):
        count = 1
        x = 0

album_list = ["Copa do Mundo 2022", "Pokemon", "Harry Potter"] # 0 = Copa do Mundo 2022, 1 = Pokemon, 2 = Harry Potter
for x in range(len(album_list)):
    album_list[x] = int(oracle.sqlToDataFrame(f"select id from labdatabase.\"album\" where title = '{album_list[x]}'").iloc[0]["id"])
    count += 1
    if count>len(album_list):
        count = 1
        x = 0

background_list = ["commom", "uncommon", "rare", "epic", "legendary"] # 0 = common, 1 = uncommon, 2 = rare, 3 = epic, 4 = legendary
for x in range(len(background_list)):
    background_list[x] = int(oracle.sqlToDataFrame(f"select id from labdatabase.\"background\" where rarity_id = '{x + 1}'").iloc[0]["id"])
    count += 1
    if count>len(background_list):
        count = 1
        x = 0

border_list = ["commom", "uncommon", "rare", "epic", "legendary"] # 0 = common, 1 = uncommon, 2 = rare, 3 = epic, 4 = legendary
count = 1
for x in range(len(border_list)):
    border_list[x] = int(oracle.sqlToDataFrame(f"select id from labdatabase.\"border\" where rarity_id = '{x + 1}'").iloc[0]["id"])
    count += 1
    if count>len(border_list):
        count = 1
        x = 0

oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 4, 'mbappe.png', 'Kylian Mbappe', :1, :2, :3, :4)", [background_list[1], border_list[1], rarity_list[1], album_list[0]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 5, 'ronaldinho.png', 'Ronaldinho Gaucho', :1, :2, :3, :4)", [background_list[4], border_list[4], rarity_list[4], album_list[0]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 6, 'ibrahimovic.png', 'Zlatan Ibrahimovic', :1, :2, :3, :4)", [background_list[3], border_list[3], rarity_list[3], album_list[0]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 7, 'zidane.png', 'Zinédine Zidane', :1, :2, :3, :4)", [background_list[0], border_list[0], rarity_list[0], album_list[0]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 8, 'kaka.png', 'Kaka', :1, :2, :3, :4)", [background_list[0], border_list[0], rarity_list[0], album_list[0]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 9, 'pele.png', 'Pele', :1, :2, :3, :4)", [background_list[2], border_list[2], rarity_list[2], album_list[0]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 10, 'maradona.png', 'Diego Maradona', :1, :2, :3, :4)", [background_list[1], border_list[1], rarity_list[1], album_list[0]])

oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 4, 'squirtle.png', 'Squirtle', :1, :2, :3, :4)", [background_list[0], border_list[0], rarity_list[0], album_list[1]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 5, 'pidgey.png', 'Pidgey', :1, :2, :3, :4)", [background_list[1], border_list[1], rarity_list[1], album_list[1]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 6, 'psyduck.png', 'Psyduck', :1, :2, :3, :4)", [background_list[2], border_list[2], rarity_list[2], album_list[1]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 7, 'onix.png', 'Onix', :1, :2, :3, :4)", [background_list[0], border_list[0], rarity_list[0], album_list[1]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 8, 'eevee.png', 'Eevee', :1, :2, :3, :4)", [background_list[2], border_list[2], rarity_list[2], album_list[1]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 9, 'dratini.png', 'Dratini', :1, :2, :3, :4)", [background_list[0], border_list[0], rarity_list[0], album_list[1]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 10, 'articuno.png', 'Articuno', :1, :2, :3, :4)", [background_list[4], border_list[4], rarity_list[4], album_list[1]])

oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 4, 'hagrid.png', 'Rubeo Hagrid', :1, :2, :3, :4)", [background_list[1], border_list[1], rarity_list[1], album_list[2]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 5, 'dumbledore.png', 'Albus Dumbledore', :1, :2, :3, :4)", [background_list[4], border_list[4], rarity_list[4], album_list[2]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 6, 'voldemort.png', 'Lord Voldemort', :1, :2, :3, :4)", [background_list[3], border_list[3], rarity_list[3], album_list[2]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 7, 'snape.png', 'Severus Snape', :1, :2, :3, :4)", [background_list[2], border_list[2], rarity_list[2], album_list[2]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 8, 'bellatrix.png', 'Bellatrix Lestrange', :1, :2, :3, :4)", [background_list[0], border_list[0], rarity_list[0], album_list[2]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 9, 'dobby.png', 'Dobby', :1, :2, :3, :4)", [background_list[0], border_list[0], rarity_list[0], album_list[2]])
oracle.write("insert into \"card\" (id, \"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(card_id_seq.NEXTVAL, 10, 'sirius.png', 'Sirius Black', :1, :2, :3, :4)", [background_list[0], border_list[0], rarity_list[0], album_list[2]])

attacker_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Attacker'")
mid_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Mid'")
water_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Water'")
grass_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Grass'")
fire_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Fire'")
electric_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Electric'")
poison_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Poison'")
flying_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Flying'")
normal_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Normal'")
dragon_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Dragon'")
ice_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Ice'")
stone_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Stone'")
wizard_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Wizard'")
elf_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Elf'")
death_eaters_tag_id = oracle.sqlToDataFrame("select id from labdatabase.\"tag\" where \"name\" = 'Death Eaters'")

oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Neymar Junior'").iloc[0]["id"]), int(attacker_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Lionel Messi'").iloc[0]["id"]), int(attacker_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Cristiano Ronaldo'").iloc[0]["id"]), int(attacker_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Kylian Mbappe'").iloc[0]["id"]), int(attacker_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Zlatan Ibrahimovic'").iloc[0]["id"]), int(attacker_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Pele'").iloc[0]["id"]), int(attacker_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Diego Maradona'").iloc[0]["id"]), int(mid_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Ronaldinho Gaucho'").iloc[0]["id"]), int(mid_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Zinédine Zidane'").iloc[0]["id"]), int(mid_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Kaka'").iloc[0]["id"]), int(mid_tag_id.iloc[0]["id"])])


oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Squirtle'").iloc[0]["id"]), int(water_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Psyduck'").iloc[0]["id"]), int(water_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Eevee'").iloc[0]["id"]), int(normal_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Pidgey'").iloc[0]["id"]), int(normal_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Articuno'").iloc[0]["id"]), int(flying_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Articuno'").iloc[0]["id"]), int(ice_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Dratini'").iloc[0]["id"]), int(ice_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Dratini'").iloc[0]["id"]), int(dragon_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Bulbasaur'").iloc[0]["id"]), int(grass_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Bulbasaur'").iloc[0]["id"]), int(poison_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Charmander'").iloc[0]["id"]), int(fire_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Pikachu'").iloc[0]["id"]), int(electric_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Onix'").iloc[0]["id"]), int(stone_tag_id.iloc[0]["id"])])


oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Harry Potter'").iloc[0]["id"]), int(wizard_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Rony Weasley'").iloc[0]["id"]), int(wizard_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Hermione Granger'").iloc[0]["id"]), int(wizard_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Rubeo Hagrid'").iloc[0]["id"]), int(wizard_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Albus Dumbledore'").iloc[0]["id"]), int(wizard_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Severus Snape'").iloc[0]["id"]), int(wizard_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Sirius Black'").iloc[0]["id"]), int(wizard_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Dobby'").iloc[0]["id"]), int(elf_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Lord Voldemort'").iloc[0]["id"]), int(death_eaters_tag_id.iloc[0]["id"])])
oracle.write("insert into \"card_tag\" (card_id, tag_id) values(:1, :2)", [int(oracle.sqlToDataFrame("select id from labdatabase.\"card\" where \"name\" = 'Bellatrix Lestrange'").iloc[0]["id"]), int(death_eaters_tag_id.iloc[0]["id"])])

