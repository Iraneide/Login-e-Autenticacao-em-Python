from time import time

from flask import Blueprint, current_app, render_template, request, session, redirect, url_for, flash
from app import bcrypt
from app.database.conexao import conectar


main = Blueprint('main', __name__)

@main.get('/login')
@main.route('/')
def index():
    if 'usuario_id' in session:
        return redirect(url_for('painel.index'))
    if request.args.get('sessao_expirada') == '1':
        flash('Sua sessão expirou. Faça o login novamente.', 'danger')
        return redirect(url_for('main.index'))
    return render_template('index.html')

@main.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('password')
    lembrar = request.form.get('remember')

    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios where email = %s", (email,))
    usuario = cursor.fetchone()
    cursor.close()
    conexao.close()

    if usuario and usuario['ativo'] != 'Sim':
        flash('Usuário inativo contate o  Administrador')
        return redirect(url_for('main.index'))


    senha_valida = False
    if usuario and usuario['senha'] and senha:
        try:
            senha_valida = bcrypt.check_password_hash(usuario['senha'], senha)
        except ValueError:
            current_app.logger.warning('Não foi possível validar a senha do usuário %s com bcrypt.', usuario['id'])

    if senha_valida:
        session.permanent = bool(lembrar)
        session['usuario_id'] = usuario['id']
        session['usuario_nome'] = usuario['nome']
        session['usuario_nivel'] = usuario['nivel']
        session['sessao_expira_em'] = time() + current_app.permanent_session_lifetime.total_seconds()

        return redirect(url_for('painel.index'))
    flash('E-mail ou senha incorretos!', 'danger')
    return redirect(url_for('main.index'))
