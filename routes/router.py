from flask import render_template, Blueprint, request, redirect, url_for
import csv

caminho_tabela_especialidades = "db_tables/tb_especialidades.csv"
caminho_tabela_medicos = "db_tables/tb_medicos.csv"
caminho_tabela_horarios = "db_tables/tb_horatios.csv"


home_blue_print = Blueprint("home", __name__ )
cadastro_especialidade_blue_print = Blueprint("cadastro_especialidade", __name__ )
home_blue_print = Blueprint("home", __name__ )
cadastro_medicos_blue_print = Blueprint("cadastro_medicos", __name__ )
cadastro_horarios_blue_print = Blueprint("cadastro_horarios", __name__ )
listar_especialidades_blue_print = Blueprint("listar_especialidades", __name__ )
deletar_especialidade_blue_print = Blueprint("deletar_especialidade", __name__ )

@home_blue_print.route("/")
def home_page():
    return render_template("index.html")


@cadastro_especialidade_blue_print.route("/cadastro_especialidade", methods=['GET','POST'])
def cadastro_especialidade_page():
    if request.method == "POST":
        especialidade = request.form.get("especialidade")
        with open(caminho_tabela_especialidades, "a", newline= "") as arquivo:
            escritor = csv.writer(arquivo,delimiter=",")
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


@cadastro_horarios_blue_print.route("/cadastro_horarios", methods=["GET", "POST"])
def cadastrar_horarios_pagina():
    with open(caminho_tabela_medicos, "r", newline="", encoding="utf-8") as arquivo:
        medicos = []
        csv_reader = csv.reader(arquivo)

        next(csv_reader)

        for linha in csv_reader:
            medicos.append(linha[0])

        if request.method == "POST":
            horario = request.form.get("tempo")
            medico = request.form.get("medicos")
            with open(caminho_tabela_horarios, "a", newline= "", encoding= "utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow([horario,medico])

    return render_template("cadastro_horarios_medicos.html", medicos=medicos)


@listar_especialidades_blue_print.route("/listar_especialidades" , methods = ["GET", "POST"])
def listar_especialidades_pagina():
    with open(caminho_tabela_especialidades, "r", newline="", encoding="utf-8") as arquivo:
        especialidades = []
        csv_reader = csv.reader(arquivo)

        next(csv_reader)

        for linha in csv_reader:
            especialidades.append(linha[0])

    return render_template("lista_especialidades.html", especialidades=especialidades)


@deletar_especialidade_blue_print.route("/deletar_especialidade", methods = ["GET", "POST"])
def deletar_especialidade_pagina():
    with open(caminho_tabela_especialidades, "r", newline="", encoding="utf-8") as arquivo:
        especialidades = []
        csv_reader = csv.reader(arquivo)

        

        for linha in csv_reader:
            if linha[0] != "especialidades":
                especialidades.append(linha[0])
    
    return render_template("deletar_especialidade.html", especialidades=especialidades)


@deletar_especialidade_blue_print.route("/deletar_especialidade/<nome>", methods = ["POST"])
def deletar_especialidade(nome):
    with open(caminho_tabela_especialidades, "r", newline="", encoding="utf-8") as arquivo:
        especialidades = []
        csv_reader = csv.reader(arquivo)

        filds = next(csv_reader)

        for linha in csv_reader:
            if linha[0] != nome:
                especialidades.append(linha[0])
    
    with open(caminho_tabela_especialidades, "w", newline="", encoding="utf-8") as arquivo:
        csv_writer = csv.writer(arquivo, delimiter=',')
        csv_writer.writerow(filds)
        csv_writer.writerow(especialidades)

    return redirect(url_for("deletar_especialidade.deletar_especialidade_pagina"))