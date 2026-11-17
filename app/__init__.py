from datetime import timedelta
from time import time

from flask import Flask, session
from flask_bcrypt import Bcrypt
from app.database.conexao import conectar
from config import EMAIL_SISTEMA, NOME_SISTEMA, SECRET_KEY, SENHA_PADRAO

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = SECRET_KEY

    bcrypt.init_app(app)

    from app.routes.main import main
    app.register_blueprint(main)

    from app.routes.painel.routes import painel
    app.register_blueprint(painel)

    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)

    @app.before_request
    def expirar_sessao():
        if 'usuario_id' in session and time() >= session.get('sessao_expira_em', 0):
            session.clear()

    criar_admin_padrao()

    return app
# Inicializa o pacote app e disponibiliza a criação da aplicação.

def criar_admin_padrao():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios where nivel = 'Administrador' LIMIT 1")
    usuario = cursor.fetchone()

    if not usuario:
        sennha_criptografada = bcrypt.generate_password_hash(SENHA_PADRAO).decode('utf-8')
        cursor.execute("INSERT INTO usuarios SET nome = %s, email = %s, senha = %s, nivel = 'Administrador', ativo = 'Sim'",
                       (NOME_SISTEMA, EMAIL_SISTEMA, sennha_criptografada))
    conexao.commit()

    cursor.close()
    conexao.close()
