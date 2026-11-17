from app import create_app

# Cria a aplicação usando a função definida no pacote app.
app = create_app()

# Inicia o servidor local quando este arquivo é executado diretamente.
if __name__ == "__main__":
    app.run()
