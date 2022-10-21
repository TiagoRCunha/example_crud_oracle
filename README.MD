# Sobre este projeto

Este projeto é um __fork__ [deste repositório](https://github.com/howardroatti/example_crud_oracle), para fins de obtenção de nota na disciplina de banco de dados ministrada pelo professor Howard Roatti.

Os integrantes são:
- [Henrique Klayton](https://github.com/henrique-klayton)
- [Tiago R Cunha](https://github.com/TiagoRCunha)
- [Victor Binda S](https://github.com/Victorbnd)


# Album digital

Esse sistema é sobre completar um album digital, adicionando cartas únicas com o intuito de trabalhar com os conteúdos aprendidos em aula. O usuário pode comprar figurinhas, para completar o album, e cada figurinha tem propriedades diferentes.

--- 

O sistema exige que as tabelas existam, então basta executar o script Python a seguir para criação das tabelas e preenchimento de dados de exemplos:
```shell
~$ python create_tables_and_records.py
```

Para executar o sistema basta executar o script Python a seguir:
```shell
~$ python run.py
```


## Organização
- [diagrams](diagrams): Nesse diretório está o [diagrama relacional](diagrams/diagrama_er.pdf) (lógico) do sistema.
    * O sistema possui onze entidades: album, user, card, border, background, tag, rarity, border_tag, card_tag, background_tag, user_card
- [sql](sql): Nesse diretório estão os scripts para criação das tabelas e inserção de dados fictícios para testes do sistema
    * [create_tables.sql](sql/create_tables.sql): script responsável pela criação das tabelas e relacionamentos.
    * [insert_values.sql](sql/insert_values.sql): script responsável pela inserção dos registros fictícios para testes do sistema.
- [src](src): Nesse diretório estão os scripts do sistema
    * [conexion](src/conexion): Nesse repositório encontra-se o [módulo de conexão com o banco de dados Oracle](src/conexion/oracle_queries.py). Esse módulo possui algumas funcionalidades úteis para execução de instruções DML e DDL, sendo possível obter JSON, Matriz e Pandas DataFrame.
      - Exemplo de utilização para consultas simples:

        ```python
        def listar_clientes(self, oracle:OracleQueries, need_connect:bool=False):
            query = """
                    select c.cpf
                        , c.nome 
                    from clientes c
                    order by c.nome
                    """
            if need_connect:
                oracle.connect()
            print(oracle.sqlToDataFrame(query))
        ```
      - Exemplo de utilização para alteração de registros

        ```python
        from conexion.oracle_queries import OracleQueries
        def inserir_cliente(self) -> Cliente:
            # Cria uma nova conexão com o banco que permite alteração
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            # Solicita ao usuario o novo CPF
            cpf = input("CPF (Novo): ")

            if self.verifica_existencia_cliente(oracle, cpf):
                # Solicita ao usuario o novo nome
                nome = input("Nome (Novo): ")
                # Insere e persiste o novo cliente
                oracle.write(f"insert into clientes values ('{cpf}', '{nome}')")
                # Recupera os dados do novo cliente criado transformando em um DataFrame
                df_cliente = oracle.sqlToDataFrame(f"select cpf, nome from clientes where cpf = '{cpf}'")
                # Cria um novo objeto Cliente
                novo_cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0])
                # Exibe os atributos do novo cliente
                print(novo_cliente.to_string())
                # Retorna o objeto novo_cliente para utilização posterior, caso necessário
                return novo_cliente
            else:
                print(f"O CPF {cpf} já está cadastrado.")
                return None
        ```
      - Outros exemplos: [test.py](src/test.py)
      - Caso esteja utilizando na máquina virtual antiga, você precisará alterar o método connect de:
          ```python
          self.conn = cx_Oracle.connect(user=self.user,
                                  password=self.passwd,
                                  dsn=self.connectionString()
                                  )
          ```
        Para:
          ```python
          self.conn = cx_Oracle.connect(user=self.user,
                                  password=self.passwd,
                                  dsn=self.connectionString(in_container=True)
                                  )
          ```
    * [controller](src/controller/): Nesse diretório encontram-sem as classes controladoras, responsáveis por realizar inserção, alteração e exclusão dos registros das tabelas.
    * [model](src/model/): Nesse diretório encontram-ser as classes das entidades descritas no [diagrama relacional](diagrams/album-der.pdf)
    * [reports](src/reports/) Nesse diretório encontra-se a [classe](src/reports/relatorios.py) responsável por gerar todos os relatórios do sistema
    * [sql](src/sql/): Nesse diretório encontram-se os scripts utilizados para geração dos relatórios
    * [utils](src/utils/): Nesse diretório encontram-se scripts de [configuração](src/utils/config.py) e automatização da tela de informações iniciais
    * [create_tables_and_records.py](src/create_tables_and_records.py): Script responsável por criar as tabelas e registros fictícios. Esse script deve ser executado antes do script [run.py](src/run.py) para gerar as tabelas, caso não execute os scripts diretamente no SQL Developer ou em alguma outra IDE de acesso ao Banco de Dados.
    * [run.py](src/run.py): Script responsável por ser a interface entre o usuário e os módulos de acesso ao Banco de Dados. Deve ser executado após a criação das tabelas.
    * [populate_with_Oracle_queries]: Script que faz mais algumas inserções no banco, porém utilizando a biblioteca a fim de praticar.

### Bibliotecas Utilizadas
- [requirements.txt](src/requirements.txt): `pip install -r requirements.txt`

### Instalando Oracle InstantClient
- Baixe a versão do [InstantClient](https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html) de acordo com a versão do Banco de Dados
- Caso esteja utilizando uma distribuição Linux baseado em Debian, será necessário executar o comando a seguir para converter o arquivo .rpm para .deb.
  ```shell
  sudo alien --scripts oracle-instantclient18.5-basic-18.5.0.0.0-3.x86_64.rpm
  ```
- Descompacte o arquivo e será gerado um diretório em um diretório de fácil acesso.
- Mova os diretórios lib e share para dentro do diretório do InstantClient
  ```shell
  sudo mv lib /usr/local/oracle/instantclient_18_5/
  ```
  
  ```shell
  sudo mv share instantclient_18_5/
  ```
- Edite o arquivo `.bash_profile` incluindo as linhas a seguir ao final do arquivo:
  ```shell
  export ORACLE_HOME=/usr/local/oracle/instantclient_18_5/lib/oracle/18.5/client64
  export LD_LIBRARY_PATH=$ORACLE_HOME/lib
  export PATH=$PATH:$ORACLE_HOME/bin
  export PATH
  ```

## Contato do grupo
Tiago R. Cunha
- [LinkedIn](https://linkedin.com/in/tiago-rodrigues-cunha)
- [E-Mail](mailto:tiago.r.c.sn@gmail.com)
Henrique
- [LinkedIn](https://linkedin.com/in/henrique-klayton)
- [E-Mail](mailto:henrique70031@gmail.com)
Victor
- [LinkedIn](https://linkedin.com/in/victorbnd)
- [E-Mail](mailto:victorbinda2017@gmail.com)

## Contato do professor
- [LinkedIn](https://linkedin.com/in/howardroatti)
- [E-Mail](mailto:howardcruzroatti@gmail.com)