from typing import Optional
from controller.controller_rarity import RarityController
from controller.controller_background import BackgroundController
from controller.controller_tag import TagController
from controller.controller_album import AlbumController
from controller.controller_border import BorderController
from controller.controller_card import CardController
import utils.config as config
from utils.records import Records

def select_album_update():
    loop = True
    while loop:
        print(config.MENU_ADMIN_ALBUNS_AVAIBLES)
        albuns_list = Records().list_albuns()
        for x in range(albuns_list.shape[0]):
            print(f"{x + 1} - " + albuns_list.iloc[x]["title"])
        print(config.MENU_SPLIT)
        id = input("Digite o número do album que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_album(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_album(id)
        if not id_verification.empty:
            config.clear_console(1)
            if update_album(id) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None
  
def update_album(id):
    show_album = Records().show_album(id)

    print("As informações do album disponíveis para alteração são:\n")
    for x in range(show_album.shape[0]):
        print(show_album.iloc[0])
    print("\n", config.MENU_ADMIN_CHANGE_RECORDS_ALBUM_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_title = input("Insira o novo titulo para o album\n")
            if new_title == "0":
                config.clear_console(1)
                return 0
            AlbumController().update(id, new_title, None, 1)
            break
        elif selection == 2:
            new_description = input("Insira a nova descrição do album\n")
            if new_description == "0":
                config.clear_console(1)
                return 0
            AlbumController().update(id, None, new_description, 2)
            break
        elif selection == 0:
            config.clear_console(1)
            return 0

def select_user_update():
    loop = True
    while loop:
        print(config.MENU_ADMIN_USERS_AVAIBLES)
        users_list = Records().list_users()
        for x in range(users_list.shape[0]):
            print(f"{x + 1} - " + users_list.iloc[x]["username"])
        print(config.MENU_SPLIT)
        id = input("Digite o número do usuário que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_user(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_user(id)
        if not id_verification.empty:
            config.clear_console(1)
            if update_user(id) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None


#TODO
def update_user(id):
    show_user = Records().show_user(id)

    print("As informações do usuário disponíveis para alteração são:\n")
    for x in range(show_user.shape[0]):
        print(show_user.iloc[0])
    print("\n", config.MENU_ADMIN_CHANGE_RECORDS_USER_OPTIONS)
    selection = int(input("Digite sua opção, ou aperte 'Enter' para sair\n"))
    loop = True
    while loop:
        if selection == 1:
            new_username = input("Insira o novo username para o usuário\n")
            if new_username == "":
                config.clear_console(1)
                return 0
            #UPDATE USERNAME USER
            break
        elif selection == 2:
            new_password = input("Insira a nova senha do usuário\n")
            if new_password == "":
                config.clear_console(1)
                return 0
            #UPDATE SENHA USER
            break
        elif selection == 3:
            new_access_type = input("Insira o novo tipo de acesso do usuário [0 = Normal, 1 = Admin]\n")
            while new_access_type != "0" and new_access_type != "1" and new_access_type != "":
                new_access_type = input("Tipo de acesso inválido, insira novamente [0 = normal, 1 = admin]\n")
            if new_access_type == "":
                config.clear_console(1)
                return 0
            #UPDATE TIPO DE ACESSO USER
            break
        elif selection == 0:
            config.clear_console(1)
            return 0

def select_card_update():
    loop = True
    while loop:
        print(config.MENU_ADMIN_CARDS_AVAIBLES)
        cards_list = Records().list_cards()
        for x in range(cards_list.shape[0]):
            print(f"{x + 1} - " + cards_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        id = input("Digite o número da carta que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_card(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_card(id)
        if not id_verification.empty:
            config.clear_console(1)
            if update_card(id) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None

#TODO
def update_card(id):
    show_card = Records().show_card(id)

    print("As informações da carta disponíveis para alteração são:\n")
    for x in range(show_card.shape[0]):
        print(show_card.iloc[0])
    print("\n", config.MENU_ADMIN_CHANGE_RECORDS_CARD_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_image = input("Insira a nova imagem da carta\n")
            if new_image == "0":
                config.clear_console(1)
                return 0
            CardController().update(id, new_image, None, 1)
            break
        elif selection == 2:
            new_name = input("Insira o novo nome da carta\n")
            if new_name == "0":
                config.clear_console(1)
                return 0
            CardController().update(id, None, new_name, 1)
            break
        elif selection == 0:
            config.clear_console(1)
            return 0

def select_border_update():
    loop = True
    while loop:
        print(config.MENU_ADMIN_BORDERS_AVAIBLES)
        border_list = Records().list_borders()
        for x in range(border_list.shape[0]):
            print(f"{x + 1} - " + border_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        id = input("Digite o número da borda que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_border(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_border(id)
        if not id_verification.empty:
            config.clear_console(1)
            if update_border(id) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None

#TODO
def update_border(id):

    show_border = Records().show_border(id)
    print("As informações da borda disponíveis para alteração são:\n")
    for x in range(show_border.shape[0]):
        print(show_border.iloc[0])
    print("\n", config.MENU_ADMIN_CHANGE_RECORDS_BORDER_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_image = input("Insira a nova imagem da borda\n")
            if new_image == "0":
                config.clear_console(1)
                return 0
            BorderController().update(id, None, new_image, 1)
            break
        elif selection == 2:
            new_name = input("Insira o novo nome da borda\n")
            if new_name == "0":
                config.clear_console(1)
                return 0
            BorderController().update(id, new_name, None, 2)
            break
        elif selection == 0:
            config.clear_console(1)
            return 0

def select_background_update():
    print(config.MENU_ADMIN_BACKGROUND_AVAIBLES)
    background_list = BackgroundController().list_table()
    for x in range(background_list.shape[0]):
        print(str(background_list.id.values[x]) + " - " + str(background_list.name.values[x]))
    print(config.MENU_SPLIT)
    id = input("Digite o número do background que deseja alterar ou 0 para sair\n")
    loop = True
    while loop:
        id_verification = Records().show_background(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_background(id)
        if not id_verification.empty:
            config.clear_console(1)
            if update_background(id) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None

def update_background(id):
    show_background = BackgroundController().get_by_id(id).to_string()

    print("As informações do background disponíveis para alteração são:\n")
    print(show_background)
    print("\n", config.MENU_ADMIN_CHANGE_RECORDS_BACKGROUND_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_image = input("Insira a nova imagem do background\n")
            if new_image == "0":
                config.clear_console(1)
                return 0
            BackgroundController().update(id, image=new_image)
            break
        elif selection == 2:
            new_name = input("Insira o novo nome do background\n")
            if new_name == "0":
                config.clear_console(1)
                return 0
            BackgroundController().update(id, name=new_name)
            break
        elif selection == 3:
            RarityController().list_table()
            new_rarity = input("Insira a nova raridade do background\n")
            if new_rarity == "0":
                config.clear_console(1)
                return 0
            BackgroundController().update(id, rarity_id=new_rarity)
            break
        elif selection == 0:
            config.clear_console(1)
            return 0

def select_tag_update():
    loop = True
    while loop:
        print(config.MENU_ADMIN_TAG_AVAIBLES)
        tag_list = Records().list_tags()
        for x in range(tag_list.shape[0]):
            print(f"{x + 1} - " + tag_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        id = input("Digite o número da tag que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_tag(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_tag(id)
        if not id_verification.empty:
            config.clear_console(1)
            if update_tag(id) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None

def update_tag(id):
    show_tag = TagController().get_by_id(id).to_string()

    print("As informações da tag disponíveis para alteração são:\n")
    print(show_tag)
    print("\n", config.MENU_ADMIN_CHANGE_RECORDS_TAG_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_name = input("Insira o novo nome da tag\n")
            if new_name == "0":
                config.clear_console(1)
                return 0
            print(TagController().update(id, new_name).to_string())
            break
        elif selection == 0:
            config.clear_console(1)
            return 0

def select_rarity_update():
    loop = True
    while loop:
        print(config.MENU_ADMIN_RARITY_AVAIBLES)
        rarity_list = Records().list_rarity()
        for x in range(rarity_list.shape[0]):
            print(f"{x + 1} - " + rarity_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        id = input("Digite o número da raridade que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_rarity(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_rarity(id)
        if not id_verification.empty:
            config.clear_console(1)
            if update_rarity(id) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None

def update_rarity(id):
    controller = RarityController()
    name: Optional[str] = None
    tier: Optional[str] = None

    print("As informações da raridade disponíveis para alteração são:\n")
    print(controller.get_by_id(id).to_string())
    print("\n", config.MENU_ADMIN_CHANGE_RECORDS_RARITY_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_name = input("Insira o novo nome da raridade\n")
            if new_name == "0":
                config.clear_console(1)
                return 0
            break
        if selection == 2:
            new_tier = input("Insira o novo tier da raridade\n")
            if new_tier == "0":
                config.clear_console(1)
                new_tier = None
                return 0
            break
        elif selection == 0:
            config.clear_console(1)
            controller.update(id, name, tier)
            return 0

def menu_continue():
    config.clear_console(1)
    print(config.MENU_ADMIN_UPDATE_RECORDS_CONTINUE)
    selection = str(input("Insira sua opção\n"))
    if selection == "2":
        config.clear_console(1)
        return 2
    config.clear_console(1)
