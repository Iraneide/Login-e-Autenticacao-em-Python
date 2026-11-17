# Login e autenticação em Python

Aplicação Flask com login via MySQL, senhas protegidas com bcrypt e painel restrito. A sessão expira um minuto após o login e o painel volta automaticamente para a tela de entrada.

## Executar localmente no Windows

Com Python 3.11 ou superior e MySQL em execução, abra o PowerShell na pasta do repositório e instale as dependências.

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Execute [database/schema.sql](database/schema.sql) no phpMyAdmin ou use o cliente MySQL com um usuário autorizado a criar o banco.

```powershell
mysql -u usuario_mysql -p -e "source database/schema.sql"
```

Configure as variáveis abaixo no mesmo terminal. O SQL cria o banco `valtrevo`, usado por padrão. Se o MySQL estiver em outro endereço, defina também `DB_HOST`.

```powershell
$env:DB_USER = 'usuario_mysql'
$env:DB_PASSWORD = Read-Host 'Senha do MySQL'
$env:EMAIL_SISTEMA = Read-Host 'E-mail do administrador'
$env:SENHA_PADRAO = Read-Host 'Senha inicial do administrador'
$env:SECRET_KEY = .\.venv\Scripts\python.exe -c "import secrets; print(secrets.token_hex(32))"
.\.venv\Scripts\python.exe run.py
```

Abra [a tela de login local](http://127.0.0.1:5000/). Na primeira execução com o banco vazio, o sistema cria o administrador com o e-mail e a senha informados. Se já houver um administrador, as credenciais existentes são preservadas.
