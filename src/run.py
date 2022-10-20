import menus
from records import Records
import update_records
import create_records
import remove_records

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

                elif selection == 0:
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
                elif selection == 2:
                        #Relatórios de cartas
                        break
                elif selection == 3:
                        #Relatórios de usuários
                        break
                elif selection == 0:
                        loop = False
                        break

def admin_access_change_records():
        loop = True
        while loop:
                print(menus.MENU_ADMIN_CHANGE_RECORDS)
                print("As tabelas disponiveis para modificação são:\n")
                table_list = menus.search_tables()
                for x in range(7):
                        print(f"{x + 1} - " + table_list.iloc[x]["table_name"])
                print(menus.MENU_SPLIT)
                selection = int(input("Digite o nome da tabela que deseja modificar, insira 0 para sair\n"))
                menus.clear_console(1)
                if selection == 1:
                        update_records.select_album_update()
                elif selection == 2:
                        update_records.select_rarity_update()
                elif selection == 3:
                        update_records.select_user_update()
                elif selection == 4:
                        update_records.select_border_update()
                elif selection == 5:
                        update_records.select_background_update()
                elif selection == 6:
                        update_records.select_card_update()
                elif selection == 7:
                        update_records.select_tag_update()
                elif selection == 0:
                        loop = False
                        menus.clear_console(1)

def admin_access_create_records():
        loop = True
        while loop:
                print(menus.MENU_ADMIN_CREATE_RECORDS)
                print("As tabelas disponiveis para inserção de valores são:\n")
                table_list = menus.search_tables()
                for x in range(table_list.shape[0]):
                        print(f"{x + 1} - " + table_list.iloc[x]["table_name"])
                print(menus.MENU_SPLIT)
                selection = int(input("Digite o nome da tabela que deseja inserir um valor, insira 0 para sair\n"))
                menus.clear_console(1)
                if selection == 1:
                        create_records.create_album()
                elif selection == 2:
                        create_records.create_rarity()
                elif selection == 3:
                        create_records.create_user()
                elif selection == 4:
                        create_records.create_border()
                elif selection == 5:
                        create_records.create_background()
                elif selection == 6:
                        create_records.create_card()
                elif selection == 7:
                        create_records.create_tag()
                elif selection == 8:
                        menus.clear_console(1)
                        create_records.create_border_tag()
                elif selection == 9:
                        menus.clear_console(1)
                        create_records.create_card_tag()
                elif selection == 10:
                        menus.clear_console(1)
                        create_records.create_background_tag()
                elif selection == 11:
                        menus.clear_console(1)
                        create_records.create_user_card()
                elif selection == 0:
                        loop = False
                        menus.clear_console(1)
                        
def admin_access_delete_records():
        loop = True
        while loop:
                print(menus.MENU_ADMIN_DELETE_RECORDS)
                print("As tabelas disponiveis para remoção de valores são:\n")
                table_list = menus.search_tables()
                for x in range(table_list.shape[0]):
                        print(f"{x + 1} - " + table_list.iloc[x]["table_name"])
                print(menus.MENU_SPLIT)
                selection = int(input("Digite o nome da tabela que deseja remover um valor, insira 0 para sair\n"))
                if selection == 1:
                        menus.clear_console(1)
                        remove_records.remove_album()
                elif selection == 2:
                        menus.clear_console(1)
                        remove_records.remove_rarity()
                elif selection == 3:
                        menus.clear_console(1)
                        remove_records.remove_user()
                elif selection == 4:
                        menus.clear_console(1)
                        remove_records.remove_border()
                elif selection == 5:
                        menus.clear_console(1)
                        remove_records.remove_background()
                elif selection == 6:
                        menus.clear_console(1)
                        remove_records.remove_card()
                elif selection == 7:
                        menus.clear_console(1)
                        remove_records.remove_tag()
                elif selection == 8:
                        menus.clear_console(1)
                        remove_records.remove_border_tag()
                elif selection == 9:
                        menus.clear_console(1)
                        remove_records.remove_card_tag()
                elif selection == 10:
                        menus.clear_console(1)
                        remove_records.remove_background_tag()
                elif selection == 11:
                        menus.clear_console(1)
                        remove_records.remove_user_card()
                elif selection == 0:
                        loop = False
                        menus.clear_console(1)
                menus.clear_console(1)
        
run()
