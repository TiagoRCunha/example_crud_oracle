from conexion.oracle_queries import OracleQueries

MENU_SPLIT = """
========================================
"""
MENU_INICIAL = """
============= Menu Inicial =============
[1] - Realizar Login
[0] - Sair
========================================
"""

MENU_LOGIN = """
============ Realizar Login ============
Para retornar, digite 0
"""

MENU_ADMIN = """
============= Acesso de Adm ============
[1] - Ver Relatórios
[2] - Alterar Registros
[3] - Criar Registros
[4] - Deletar Registros
[0] - Sair
========================================
"""

MENU_ADMIN_REPORTS = """
========== Ralatórios de Adm ===========
[1] - Ver Relatórios de Album
[2] - Ver Relatórios de Cartas
[3] - Ver Relatórios de Usuários
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS_ALBUM_OPTIONS= """
========= Alterações Permitidas ========
[1] - Alterar Titulo
[2] - Alterar Descrição
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS_USER_OPTIONS= """
========= Alterações Permitidas ========
[1] - Alterar Username
[2] - Alterar Senha
[3] - Alterar Tipo de Acesso
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS_CARD_OPTIONS= """
========= Alterações Permitidas ========
[1] - Alterar Imagem
[2] - Alterar Nome
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS_BORDER_OPTIONS= """
========= Alterações Permitidas ========
[1] - Alterar Imagem
[2] - Alterar Nome
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS_BACKGROUND_OPTIONS= """
========= Alterações Permitidas ========
[1] - Alterar Imagem
[2] - Alterar Nome
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS_TAG_OPTIONS= """
========= Alterações Permitidas ========
[1] - Alterar Nome
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS_RARITY_OPTIONS= """
========= Alterações Permitidas ========
[1] - Alterar Nome
[2] - Alterar Tier
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS_BORDER_TAG_OPTIONS= """
========= Alterações Permitidas ========
[1] - Alterar a Tag Vinculada
[2] - Alterar a Borda Vinculada
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS_CARD_TAG_OPTIONS= """
========= Alterações Permitidas ========
[1] - Alterar a Tag Vinculada
[2] - Alterar a Borda Vinculada
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS = """
=========== Alterar Registros ==========
"""

MENU_ADMIN_ALBUNS_AVAIBLES = """
========== Albúns Disponíveis ==========
"""

MENU_ADMIN_USERS_AVAIBLES = """
========= Usuários Disponíveis =========
"""

MENU_ADMIN_CARDS_AVAIBLES = """
========== Cartas Disponíveis ==========
"""

MENU_ADMIN_BORDERS_AVAIBLES = """
========== Bordas Disponíveis ==========
"""

MENU_ADMIN_BACKGROUND_AVAIBLES = """
========== Background Disponíveis ==========
"""

MENU_ADMIN_TAG_AVAIBLES = """
============= Tags Disponíveis =============
"""

MENU_ADMIN_RARITY_AVAIBLES = """
========== Raridades Disponíveis ===========
"""

MENU_ADMIN_BORDER_TAG_AVAIBLES = """
========== Border Tag Disponíveis ===========
"""

MENU_ADMIN_CARD_TAG_AVAIBLES = """
=========== Card Tag Disponíveis ============
"""

MENU_ADMIN_CREATE_RECORDS = """
============== Criar Registros ==============
"""

MENU_ADMIN_DELETE_RECORDS = """
============= Deletar Registros =============
"""



def login(username, password):
    oracle = OracleQueries()
    oracle.connect()
    username_attempt = oracle.sqlToDataFrame(f"select * from labdatabase.\"user\" where username like '{username}' and \"password\" like '{password}'")
    if not username_attempt.empty:
        return int(username_attempt.iloc[0]["access_type"])
    else:
        return 2

def search_tables():
    oracle = OracleQueries()
    oracle.connect()
    return(oracle.sqlToDataFrame("select table_name from user_tables"))


def clear_console(wait_time:int=3):
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")