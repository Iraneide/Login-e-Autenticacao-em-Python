from flask import Blueprint, render_template, request, session, redirect, url_for, flash

from functools import wraps

def Login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario_id' not in session:
            flash('Você precisa estar logado para acessar o painel! Faça o login primeiro.', 'danger')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)

    return decorated_function
