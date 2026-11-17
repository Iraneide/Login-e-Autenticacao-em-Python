from os import environ


SECRET_KEY = environ['SECRET_KEY']
NOME_SISTEMA = environ.get('NOME_SISTEMA', 'Administrador')
EMAIL_SISTEMA = environ['EMAIL_SISTEMA']
SENHA_PADRAO = environ['SENHA_PADRAO']

DB_HOST = environ.get('DB_HOST', '127.0.0.1')
DB_USER = environ['DB_USER']
DB_PASSWORD = environ.get('DB_PASSWORD', '')
DB_NAME = environ.get('DB_NAME', 'valtrevo')
