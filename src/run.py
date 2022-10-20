import menus
from records import Records
import update_records

def run():

        print(Records().get_init())

        loop = True

        while loop:
                print(menus.MENU_INICIAL)
                selection = int(input("Selecione a opção\n"))
                menus.clear_console(1)
                if selection == 1:
                        menus.clear_console(1)
                        login()

                elif selection == 2:
                        print("Obrigado e volte sempre!")
                        menus.clear_console(1)
                        loop = False
                else:
                        selection = int(input("Opção inválida, insira novamente"))

def login():
        loop = True
        while loop:
                print(menus.MENU_LOGIN)
                username = input("Insira seu username: ")
                if username == "0":
                        loop = False
                        break
                password = input("Insira sua senha: ")
                if password == "0":
                        loop = False
                        break
                access = menus.login(username, password)
                if access == 0:
                        print("Login de usuário realizado com sucesso")
                elif access == 1:
                        print("Login de administrador realizado com sucesso")
                        menus.clear_console(1)
                        admin_access()
                else:
                        menus.clear_console(1)
                        print("Usuário ou senha incorretos, por favor tente novamente")

def admin_access():
        loop = True
        while loop:
                print(menus.MENU_ADMIN)
                selection = int(input("Selecione a opção\n"))
                menus.clear_console(1)
                if selection == 1:
                        admin_access_reports()
                elif selection == 2:
                        admin_access_change_records()
                elif selection == 3:
                        admin_access_create_records()
                elif selection == 4:
                        admin_access_delete_records()
                elif selection == 0:
                        loop = False
                        break

def admin_access_reports():
        loop = True
        while loop:
                print(menus.MENU_ADMIN_REPORTS)
                selection = int(input("Selecione a opção\n"))
                menus.clear_console(1)
                if selection == 1:
                        #Relatórios de album
                        break
                if selection == 2:
                        #Relatórios de cartas
                        break
                if selection == 3:
                        #Relatórios de usuários
                        break
                if selection == 0:
                        loop = False
                        break

def admin_access_change_records():
        loop = True
        print(menus.MENU_ADMIN_CHANGE_RECORDS)
        print("As tabelas disponiveis para modificação são:\n")
        table_list = menus.search_tables()
        for x in range(table_list.shape[0]):
                print(f"{x + 1} - " + table_list.iloc[x]["table_name"])
        print(menus.MENU_SPLIT)
        selection = int(input("Digite o nome da tabela que deseja modificar, insira 0 para sair\n"))
        menus.clear_console(1)
        while loop:
                if selection == 1:
                        update_records.select_album_update()
                elif selection == 2:
                        update_records.select_user_update()
                elif selection == 3:
                        update_records.select_card_update()
                elif selection == 4:
                        update_records.select_border_update()
                elif selection == 5:
                        update_records.select_background_update()
                elif selection == 6:
                        update_records.select_tag_update()
                elif selection == 7:
                        update_records.select_rarity_update()
                elif selection == 8:
                        update_records.select_border_tag_update()
                elif selection == 9:
                        update_records.select_card_tag_update()
                elif selection == 0:
                        loop = False

def admin_access_create_records():
        loop = True
        print(menus.MENU_ADMIN_CREATE_RECORDS)
        print("As tabelas disponiveis para inserção de valores são:\n")
        table_list = menus.search_tables()
        for x in range(table_list.shape[0]):
                print(f"{x + 1} - " + table_list.iloc[x]["table_name"])
        print(menus.MENU_SPLIT)
        selection = int(input("Digite o nome da tabela que deseja inserir um valor, insira 0 para sair\n"))
        menus.clear_console(1)
        while loop:
                if selection == 0:
                        loop = False
                        
def admin_access_delete_records():
        loop = True
        print(menus.MENU_ADMIN_DELETE_RECORDS)
        print("As tabelas disponiveis para remoção de valores são:\n")
        table_list = menus.search_tables()
        for x in range(table_list.shape[0]):
                print(f"{x + 1} - " + table_list.iloc[x]["table_name"])
        print(menus.MENU_SPLIT)
        selection = int(input("Digite o nome da tabela que deseja remover um valor, insira 0 para sair\n"))
        menus.clear_console(1)
        while loop:
                if selection == 0:
                        loop = False
        
run()
