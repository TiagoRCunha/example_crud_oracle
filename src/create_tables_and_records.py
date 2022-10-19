from conexion.oracle_queries import OracleQueries
from populate_with_Oracle_queries import populate_with_Oracle_queries

def create_tables(query:str):
    list_of_commands = query.split(";")

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:
        if len(command) > 0:
            print(command)
            try:
                oracle.executeDDL(command)
                print("Successfully executed")
            except Exception as e:
                print(e)

def generate_records(query:str, sep:str=';'):
    list_of_commands = query.split(sep)

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:
        if len(command) > 0:
            print(command)
            oracle.write(command)
            print("Successfully executed")

def run():

    with open("../sql/create_tables.sql") as f:
        query_create = f.read()

    print("Creating tables...")
    create_tables(query=query_create)
    print("Tables successfully created!")

    with open("../sql/insert_values.sql") as f:
        query_generate_records = f.read()

    print("Gerenating records")
    generate_records(query=query_generate_records, sep='--')
    print("Records successfully generated!")
   
    with open("./views/admin_album_view.sql") as f:
        query_view = f.read()

    print("Creating view...")
    create_tables(query=query_view)
    print("View admin album successfully created!")


    with open("./views/admin_card_view.sql") as f:
        query_view = f.read()

    print("Creating view...")
    create_tables(query=query_view)
    print("View admin card successfully created!")

    with open("./views/admin_users_view.sql") as f:
        query_view = f.read()

    print("Creating view...")
    generate_records(query=query_view)
    print("View admin card successfully created!")

    populate_with_Oracle_queries()
if __name__ == '__main__':
    run()