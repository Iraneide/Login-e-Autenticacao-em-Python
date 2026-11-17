from time import time

from flask import Blueprint, make_response, render_template, session, redirect, url_for, flash
from app.routes.utils.auth import Login_required

painel = Blueprint('painel', __name__)

@painel.route('/painel')
@Login_required
def index():
    nome = session.get('usuario_nome')
    nivel = session.get('usuario_nivel')

    tempo_restante_ms = max(0, round((session['sessao_expira_em'] - time()) * 1000))
    resposta = make_response(render_template(
        'painel/index.html', nome=nome, nivel=nivel, tempo_restante_ms=tempo_restante_ms
    ))
    resposta.cache_control.no_store = True
    return resposta


@painel.route('/logout', methods=['POST'])
def logout():
    session.clear()
    flash('Deslogado com sucesso!', 'success')
    return redirect(url_for('main.index'))
