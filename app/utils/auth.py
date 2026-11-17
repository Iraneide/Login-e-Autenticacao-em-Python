from functools import wraps
from flask import session, redirect, url_for


def login_required(funcao):
    @wraps(funcao)
    def verificar_login(*args, **kwargs):
        if 'usuario_id' not in session:
            return redirect(url_for('main.index'))
        return funcao(*args, **kwargs)

    return verificar_login