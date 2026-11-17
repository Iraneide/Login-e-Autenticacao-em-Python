# Importa o módulo usado para acessar o MySQL.
import mysql.connector
# Busca os dados de acesso ao banco definidos no arquivo config.py.
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

# Reúne a abertura da conexão em uma função que pode ser chamada em outros arquivos.
def conectar():

    # Tenta abrir a conexão usando as configurações abaixo.
    conexao = mysql.connector.connect(
        # Endereço do servidor onde o MySQL está instalado.
        host = DB_HOST,
        # Nome do usuário que tem acesso ao banco.
        user = DB_USER,
        # Senha desse usuário.
        password = DB_PASSWORD,
        # Nome do banco que será utilizado.
        database = DB_NAME
    )

    # Devolve a conexão para quem chamou a função usar e fechar após as consultas.
    return conexao
