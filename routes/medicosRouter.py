from flask import render_template, Blueprint, request, redirect, url_for

import csv

cadastro_medicos_blue_print = Blueprint("cadastro_medicos", __name__ )
listagem_medicos_blue_print = Blueprint("listagem_medicos", __name__ )
edicao_medicos_blue_print = Blueprint("edicao_medicos", __name__ )
excluir_medico_blue_print = Blueprint("exclusao_medico", __name__)

caminho_tabela_medicos = "db_tables/tb_medicos.csv"
caminho_tabela_especialidades = "db_tables/tb_especialidades.csv"


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



    return render_template("medicos/cadastro_medicos.html", especialidades=especialidades)


@listagem_medicos_blue_print.route("/medicos", methods = ["GET"])
def listar_medicos_pagina():
    with open(caminho_tabela_medicos, "r", newline="") as arquivo:
        medicos_e_respectivas_especialidades = []
        csv_reader = csv.DictReader(arquivo)

        for linha in csv_reader:
            medicos_e_respectivas_especialidades.append(linha)

    return render_template("medicos/medicos.html", medicos=medicos_e_respectivas_especialidades)


@edicao_medicos_blue_print.route("/edicao/medicos", methods = ["GET", "POST"])
def edicao_medico_pagina():
    with open(caminho_tabela_medicos, "r", newline="") as arquivo:
        nomes_medicos = []

        csv_leitor = csv.DictReader(arquivo)

        for linha in csv_leitor:
            nomes_medicos.append(linha)

    if request.method == "POST":
        with open(caminho_tabela_medicos, "w", newline="", encoding="utf-8") as arquivo:
            novo_nome_do_medico = request.form.get("nome")
            nome_antigo_do_medico = request.form.get("medicos")
            csv_escritor = csv.DictWriter(arquivo, fieldnames=["nome", "especilidade"])

            csv_escritor.writeheader()

            for nome in nomes_medicos:
                if nome["nome"] == nome_antigo_do_medico:
                    nome["nome"] = novo_nome_do_medico
                    
                csv_escritor.writerow(nome)
         

    return render_template("medicos/editar_medico.html", medicos=nomes_medicos)


@excluir_medico_blue_print.route("/excluir/medicos", methods = ["GET", "POST"])
def excluir_medico_pagina():
    with open(caminho_tabela_medicos, "r", newline="") as arquivo:
        nomes_medicos = []

        csv_leitor = csv.DictReader(arquivo)

        for linha in csv_leitor:
            nomes_medicos.append(linha)

    if request.method == "POST":
        with open(caminho_tabela_medicos, "w", newline="", encoding="utf-8") as arquivo:
            nome_medico_a_ser_deletado = request.form.get("medicos")
            csv_escritor = csv.DictWriter(arquivo, fieldnames=["nome", "especilidade"])

            csv_escritor.writeheader()

            for nome in nomes_medicos:
                if nome["nome"] == nome_medico_a_ser_deletado:
                    nomes_medicos.remove(nome)
                    
            csv_escritor.writerows(nomes_medicos)
         

    return render_template("medicos/excluir_medico.html", medicos=nomes_medicos)

