from flask import render_template, Blueprint, request
from controllers.cadastrar_especialidade_controller import cadastrar_especialidade_controller

home_blue_print = Blueprint("home", __name__ )
cadastro_especialidade_blue_print = Blueprint("cadastro_especialidade", __name__ )

@home_blue_print.route("/")
def home_page():
    return render_template("index.html")


@cadastro_especialidade_blue_print.route("/cadastro_especialidade", methods=['GET','POST'])
def cadastro_especialidade_page():
    cadastrar_especialidade_controller(request)
    return render_template("cadastro_especialidade.html")