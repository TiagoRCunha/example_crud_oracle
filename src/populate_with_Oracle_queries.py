from conexion.oracle_queries import OracleQueries

def getIlocId(param) -> int:
    oracle = OracleQueries(can_write=True)
    oracle.connect()
    return int(oracle.sqlToDataFrame(param).iloc[0]["id"])

def populate_with_Oracle_queries():
    oracle = OracleQueries(can_write=True)
    oracle.connect()

    query_card_select = "SELECT id, \"name\" FROM \"card\" WHERE \"name\" = "
    query_card_insert = "insert into \"card\" (\"number\", \"image\", \"name\", background_id, border_id, rarity_id, album_id) values(:1, :2, :3, :4, :5, :6, :7)"
    query_rarity_select = "SELECT id, \"tier\" FROM \"rarity\" WHERE \"tier\" = "
    query_album_select = "select id from \"album\" where title = "
    query_tag_select = "select id, \"name\" from \"tag\" where \"name\" = "
    query_card_tag_insert = "insert into \"card_tag\" (card_id, tag_id) values(:1, :2)"
    query_background_select = "select id from \"background\" where rarity_id = "
    query_border_select = "select id from \"border\" where rarity_id = "
   
    rarity_list = ["commom", "uncommon", "rare", "epic", "legendary"]
    for x in range(len(rarity_list)):
        rarity_list[x] = getIlocId(query_rarity_select + str(x + 1))

    album_list = ["Copa do Mundo 2022", "Pokemon", "Harry Potter"]
    for x in range(len(album_list)):
        album_list[x] = getIlocId(query_album_select + f"\'{album_list[x]}\'")

    background_list = ["commom", "uncommon", "rare", "epic", "legendary"]
    for x in range(len(background_list)):
        background_list[x] = getIlocId(query_background_select + str(x + 1))

    border_list = ["commom", "uncommon", "rare", "epic", "legendary"]
    for x in range(len(border_list)):
        border_list[x] = getIlocId(query_border_select + str(x + 1))

    oracle.write(query_card_insert, [4, 'mbappe.png', 'Kylian Mbappe', background_list[1], border_list[1], rarity_list[1], album_list[0]])
    oracle.write(query_card_insert, [5, 'ronaldinho.png', 'Ronaldinho Gaucho', background_list[4], border_list[4], rarity_list[4], album_list[0]])
    oracle.write(query_card_insert, [6, 'ibrahimovic.png', 'Zlatan Ibrahimovic', background_list[3], border_list[3], rarity_list[3], album_list[0]])
    oracle.write(query_card_insert, [7, 'zidane.png', 'Zinédine Zidane', background_list[0], border_list[0], rarity_list[0], album_list[0]])
    oracle.write(query_card_insert, [8, 'kaka.png', 'Kaka', background_list[0], border_list[0], rarity_list[0], album_list[0]])
    oracle.write(query_card_insert, [9, 'pele.png', 'Pele', background_list[2], border_list[2], rarity_list[2], album_list[0]])
    oracle.write(query_card_insert, [10, 'maradona.png', 'Diego Maradona', background_list[1], border_list[1], rarity_list[1], album_list[0]])

    oracle.write(query_card_insert, [4, 'squirtle.png', 'Squirtle', background_list[0], border_list[0], rarity_list[0], album_list[1]])
    oracle.write(query_card_insert, [5, 'pidgey.png', 'Pidgey', background_list[1], border_list[1], rarity_list[1], album_list[1]])
    oracle.write(query_card_insert, [6, 'psyduck.png', 'Psyduck', background_list[2], border_list[2], rarity_list[2], album_list[1]])
    oracle.write(query_card_insert, [7, 'onix.png', 'Onix', background_list[0], border_list[0], rarity_list[0], album_list[1]])
    oracle.write(query_card_insert, [8, 'eevee.png', 'Eevee', background_list[2], border_list[2], rarity_list[2], album_list[1]])
    oracle.write(query_card_insert, [9, 'dratini.png', 'Dratini', background_list[0], border_list[0], rarity_list[0], album_list[1]])
    oracle.write(query_card_insert, [10, 'articuno.png', 'Articuno', background_list[4], border_list[4], rarity_list[4], album_list[1]])

    oracle.write(query_card_insert, [4, 'hagrid.png', 'Rubeo Hagrid', background_list[1], border_list[1], rarity_list[1], album_list[2]])
    oracle.write(query_card_insert, [5, 'dumbledore.png', 'Albus Dumbledore', background_list[4], border_list[4], rarity_list[4], album_list[2]])
    oracle.write(query_card_insert, [6, 'voldemort.png', 'Lord Voldemort', background_list[3], border_list[3], rarity_list[3], album_list[2]])
    oracle.write(query_card_insert, [7, 'snape.png', 'Severus Snape', background_list[2], border_list[2], rarity_list[2], album_list[2]])
    oracle.write(query_card_insert, [8, 'bellatrix.png', 'Bellatrix Lestrange', background_list[0], border_list[0], rarity_list[0], album_list[2]])
    oracle.write(query_card_insert, [9, 'dobby.png', 'Dobby', background_list[0], border_list[0], rarity_list[0], album_list[2]])
    oracle.write(query_card_insert, [10, 'sirius.png', 'Sirius Black', background_list[0], border_list[0], rarity_list[0], album_list[2]])

    tag_names = ["Attacker", "Mid", "Water", "Grass", "Fire", "Electric", "Poison", "Flying", "Normal", "Dragon", "Ice", "Stone", "Wizard", "Elf", "Death Eaters"]
    tag_ids = []
    for x in range(len(tag_names)):
        tag_ids.append(getIlocId(query_tag_select + f"\'{tag_names[x]}\'"))

    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Neymar Junior\'"), tag_ids[0]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Lionel Messi\'"), tag_ids[0]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Cristiano Ronaldo\'"), tag_ids[0]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Kylian Mbappe\'"), tag_ids[0]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Zlatan Ibrahimovic\'"), tag_ids[0]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Pele\'"), tag_ids[0]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Diego Maradona\'"), tag_ids[1]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Ronaldinho Gaucho\'"), tag_ids[1]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Zinédine Zidane\'"), tag_ids[1]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Kaka\'"), tag_ids[1]])


    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Squirtle\'"), tag_ids[2]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Psyduck\'"), tag_ids[2]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Eevee\'"), tag_ids[3]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Pidgey\'"), tag_ids[3]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Articuno\'"), tag_ids[7]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Articuno\'"), tag_ids[10]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Dratini\'"), tag_ids[10]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Dratini\'"), tag_ids[9]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Bulbasaur\'"), tag_ids[3]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Bulbasaur\'"), tag_ids[6]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Charmander\'"), tag_ids[4]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Pikachu\'"), tag_ids[5]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Onix\'"), tag_ids[11]])


    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Harry Potter\'"), tag_ids[12]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Rony Weasley\'"), tag_ids[12]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Hermione Granger\'"), tag_ids[12]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Rubeo Hagrid\'"), tag_ids[12]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Albus Dumbledore\'"), tag_ids[12]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Severus Snape\'"), tag_ids[12]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Sirius Black\'"), tag_ids[12]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Dobby\'"), tag_ids[13]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Lord Voldemort\'"), tag_ids[14]])
    oracle.write(query_card_tag_insert, [getIlocId(query_card_select + "\'Bellatrix Lestrange\'"), tag_ids[14]])
