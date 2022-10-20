import menus
from records import Records

def select_album_update():
    print(menus.MENU_ADMIN_ALBUNS_AVAIBLES)
    albuns_list = Records().list_albuns()
    for x in range(albuns_list.shape[0]):
        print(f"{x + 1} - " + albuns_list.iloc[x]["title"])
    print(menus.MENU_SPLIT)
    id = input("Digite o número do album que deseja alterar ou 0 para sair\n")
    loop = True
    while loop:
        id_verification = Records().show_album(id)
        if id == "0":
            loop = False
            return None
        elif not id_verification.empty:
            menus.clear_console(1)
            update_album(id)
            break
        elif id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

 #TODO       
def update_album(id):
    show_album = Records().show_album(id)

    print("As informações do album disponíveis para alteração são:\n")
    for x in range(show_album.shape[0]):
        print(show_album.iloc[0])
    print("\n", menus.MENU_ADMIN_CHANGE_RECORDS_ALBUM_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_title = input("Insira o novo titulo para o album\n")
            #Records().update_album_title(new_title, id) << UPDATE TITULO ALBUM
        elif selection == 2:
            new_description = input("Insira a nova descrição do album\n")
            #Records().update_album_title(new_description, id)  << UPDATE DESCRIÇÃO ALBUM
        elif selection == 0:
            loop = False

def select_user_update():
    print(menus.MENU_ADMIN_USERS_AVAIBLES)
    users_list = Records().list_users()
    for x in range(users_list.shape[0]):
        print(f"{x + 1} - " + users_list.iloc[x]["username"])
    print(menus.MENU_SPLIT)
    id = input("Digite o número do usuário que deseja alterar ou 0 para sair\n")
    loop = True
    while loop:
        id_verification = Records().show_user(id)
        if id == "0":
            loop = False
            break
        elif not id_verification.empty:
            menus.clear_console(1)
            update_user(id)
            break
        elif id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

#TODO
def update_user(id):
    show_user = Records().show_user(id)

    print("As informações do usuário disponíveis para alteração são:\n")
    for x in range(show_user.shape[0]):
        print(show_user.iloc[0])
    print("\n", menus.MENU_ADMIN_CHANGE_RECORDS_USER_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_username = input("Insira o novo username para o usuário\n")
            #UPDATE USERNAME USER
        elif selection == 2:
            new_password = input("Insira a nova senha do usuário\n")
            #UPDATE SENHA USER
        elif selection == 3:
            new_access_type = input("Insira o novo tipo de acesso do usuário\n")
            #UPDATE TIPO DE ACESSO USER
        elif selection == 0:
            loop = False

def select_card_update():
    print(menus.MENU_ADMIN_CARDS_AVAIBLES)
    cards_list = Records().list_cards()
    for x in range(cards_list.shape[0]):
        print(f"{x + 1} - " + cards_list.iloc[x]["name"])
    print(menus.MENU_SPLIT)
    id = input("Digite o número da carta que deseja alterar ou 0 para sair\n")
    loop = True
    while loop:
        id_verification = Records().show_card(id)
        if id == "0":
            loop = False
            break
        elif not id_verification.empty:
            menus.clear_console(1)
            update_card(id)
            break
        elif id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

#TODO
def update_card(id):
    show_card = Records().show_card(id)

    print("As informações da carta disponíveis para alteração são:\n")
    for x in range(show_card.shape[0]):
        print(show_card.iloc[0])
    print("\n", menus.MENU_ADMIN_CHANGE_RECORDS_CARD_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_image = input("Insira a nova imagem da carta\n")
            #UPDATE IMAGE CARD
        elif selection == 2:
            new_name = input("Insira o novo nome da carta\n")
            #UPDATE NAME CARD
        elif selection == 0:
            loop = False

def select_border_update():
    print(menus.MENU_ADMIN_BORDERS_AVAIBLES)
    border_list = Records().list_borders()
    for x in range(border_list.shape[0]):
        print(f"{x + 1} - " + border_list.iloc[x]["name"])
    print(menus.MENU_SPLIT)
    id = input("Digite o número da borda que deseja alterar ou 0 para sair\n")
    loop = True
    while loop:
        id_verification = Records().show_border(id)
        if id == "0":
            loop = False
            break
        elif not id_verification.empty:
            menus.clear_console(1)
            update_border(id)
            break
        elif id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

#TODO
def update_border(id):
    show_border = Records().show_border(id)

    print("As informações da borda disponíveis para alteração são:\n")
    for x in range(show_border.shape[0]):
        print(show_border.iloc[0])
    print("\n", menus.MENU_ADMIN_CHANGE_RECORDS_BORDER_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_image = input("Insira a nova imagem da borda\n")
            #UPDATE IMAGE CARD
        elif selection == 2:
            new_name = input("Insira o novo nome da borda\n")
            #UPDATE NAME CARD
        elif selection == 0:
            loop = False

def select_background_update():
    print(menus.MENU_ADMIN_BACKGROUND_AVAIBLES)
    background_list = Records().list_background()
    for x in range(background_list.shape[0]):
        print(f"{x + 1} - " + background_list.iloc[x]["name"])
    print(menus.MENU_SPLIT)
    id = input("Digite o número do background que deseja alterar ou 0 para sair\n")
    loop = True
    while loop:
        id_verification = Records().show_background(id)
        if id == "0":
            loop = False
            break
        elif not id_verification.empty:
            menus.clear_console(1)
            update_background(id)
            break
        elif id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

#TODO
def update_background(id):
    show_background = Records().show_background(id)

    print("As informações do background disponíveis para alteração são:\n")
    for x in range(show_background.shape[0]):
        print(show_background.iloc[0])
    print("\n", menus.MENU_ADMIN_CHANGE_RECORDS_BACKGROUND_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_image = input("Insira a nova imagem do background\n")
            #UPDATE IMAGE BACKGROUND
        elif selection == 2:
            new_name = input("Insira o novo nome do background\n")
            #UPDATE NAME BACKGROUND
        elif selection == 0:
            loop = False

def select_tag_update():
    print(menus.MENU_ADMIN_TAG_AVAIBLES)
    tag_list = Records().list_tags()
    for x in range(tag_list.shape[0]):
        print(f"{x + 1} - " + tag_list.iloc[x]["name"])
    print(menus.MENU_SPLIT)
    id = input("Digite o número da tag que deseja alterar ou 0 para sair\n")
    loop = True
    while loop:
        id_verification = Records().show_tag(id)
        if id == "0":
            loop = False
            break
        elif not id_verification.empty:
            menus.clear_console(1)
            update_tag(id)
            break
        elif id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

#TODO
def update_tag(id):
    show_tag = Records().show_tag(id)

    print("As informações da tag disponíveis para alteração são:\n")
    for x in range(show_tag.shape[0]):
        print(show_tag.iloc[0])
    print("\n", menus.MENU_ADMIN_CHANGE_RECORDS_TAG_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_name = input("Insira o novo nome da tag\n")
            #UPDATE NAME TAG
        elif selection == 0:
            loop = False

def select_rarity_update():
    print(menus.MENU_ADMIN_RARITY_AVAIBLES)
    rarity_list = Records().list_rarity()
    for x in range(rarity_list.shape[0]):
        print(f"{x + 1} - " + rarity_list.iloc[x]["name"])
    print(menus.MENU_SPLIT)
    id = input("Digite o número da raridade que deseja alterar ou 0 para sair\n")
    loop = True
    while loop:
        id_verification = Records().show_rarity(id)
        if id == "0":
            loop = False
            break
        elif not id_verification.empty:
            menus.clear_console(1)
            update_rarity(id)
            break
        elif id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

#TODO
def update_rarity(id):
    show_rarity = Records().show_rarity(id)

    print("As informações da raridade disponíveis para alteração são:\n")
    for x in range(show_rarity.shape[0]):
        print(show_rarity.iloc[0])
    print("\n", menus.MENU_ADMIN_CHANGE_RECORDS_RARITY_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_name = input("Insira o novo nome da raridade\n")
            #UPDATE NAME RARITY
        if selection == 2:
            new_name = input("Insira o novo tier da raridade\n")
            #UPDATE TIER RARITY
        elif selection == 0:
            loop = False

def select_border_tag_update():
    print(menus.MENU_ADMIN_BORDER_TAG_AVAIBLES)
    border_tag_list = Records().list_border_tag()
    for x in range(border_tag_list.shape[0]):
        print(f"{x + 1} - " + border_tag_list.iloc[x]["name"])
    print(menus.MENU_SPLIT)
    id = input("Digite o número da border tag que deseja alterar ou 0 para sair\n")
    loop = True
    while loop:
        id_verification = Records().show_border_tag(id)
        if id == "0":
            loop = False
            break
        elif not id_verification.empty:
            menus.clear_console(1)
            update_border_tag(id)
            break
        elif id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

#TODO
def update_border_tag(id):
    show_border_tag = Records().show_border_tag(id)

    print("As informações da border tag disponíveis para alteração são:\n")
    for x in range(show_border_tag.shape[0]):
        print(show_border_tag.iloc[0])
    print("\n", menus.MENU_ADMIN_CHANGE_RECORDS_BORDER_TAG_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_name = input("Insira a nova tag id\n")
            #UPDATE TAG ID BORDERTAG
        if selection == 2:
            new_name = input("Insira a nova border id\n")
            #UPDATE BORDER ID BORDERTAG
        elif selection == 0:
            loop = False

def select_card_tag_update():
    print(menus.MENU_ADMIN_CARD_TAG_AVAIBLES)
    card_tag_list = Records().list_card_tag()
    for x in range(card_tag_list.shape[0]):
        print(f"{x + 1} - " + card_tag_list.iloc[x])
    print(menus.MENU_SPLIT)
    id = input("Digite o número da card tag que deseja alterar ou 0 para sair\n")
    loop = True
    while loop:
        id_verification = Records().show_card_tag(id)
        if id == "0":
            loop = False
            break
        elif not id_verification.empty:
            menus.clear_console(1)
            update_card_tag(id)
            break
        elif id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

#TODO
def update_card_tag(id):
    show_card_tag = Records().show_card_tag(id)

    print("As informações da card tag disponíveis para alteração são:\n")
    for x in range(show_card_tag.shape[0]):
        print(show_card_tag.iloc[0])
    print("\n", menus.MENU_ADMIN_CHANGE_RECORDS_CARD_TAG_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_name = input("Insira a nova tag id\n")
            #UPDATE TAG ID CARDTAG
        if selection == 2:
            new_name = input("Insira a nova card id\n")
            #UPDATE CARD ID CARDRTAG
        elif selection == 0:
            loop = False