from flask import Flask
from routes.router import home_blue_print, cadastro_especialidade_blue_print

app = Flask(__name__)
app.register_blueprint(home_blue_print)
app.register_blueprint(cadastro_especialidade_blue_print)

if __name__ == "__main__":
    app.run()