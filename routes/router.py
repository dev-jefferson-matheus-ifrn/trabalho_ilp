from flask import render_template, Blueprint, request
import csv
caminho_tabela_especialidades = "db_tables/tb_especialidades.csv"
caminho_tabela_medicos = "db_tables/tb_medicos.csv"


home_blue_print = Blueprint("home", __name__ )
cadastro_especialidade_blue_print = Blueprint("cadastro_especialidade", __name__ )
home_blue_print = Blueprint("home", __name__ )
cadastro_medicos_blue_print = Blueprint("cadastro_medicos", __name__ )

@home_blue_print.route("/")
def home_page():
    return render_template("index.html")


@cadastro_especialidade_blue_print.route("/cadastro_especialidade", methods=['GET','POST'])
def cadastro_especialidade_page():
    if request.method == "POST":
        especialidade = request.form.get("especialidade")
        with open(caminho_tabela_especialidades, "a", newline= "") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([especialidade])
    return render_template("cadastro_especialidade.html")


@cadastro_medicos_blue_print.route("/cadastro_medicos" , methods=['GET','POST'])
def cadastrar_medico():
    with open(caminho_tabela_especialidades, "r", newline="", encoding="utf-8") as arquivo:
        especialidades = []
        for linha in csv.reader(arquivo):
            if linha[0] != "especialidades":
                especialidades.append(linha[0])

    if request.method == "POST":
        nome_medico = request.form.get("nome")
        especialidade = request.form.get("especialidades")
        with open(caminho_tabela_medicos, "a", newline= "", encoding= "utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([nome_medico,especialidade])



    return render_template("cadastro_medicos.html", especialidades=especialidades)