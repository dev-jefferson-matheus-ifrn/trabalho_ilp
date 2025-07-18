import csv

caminho_tabela_especialidades = "db_tables/tb_especialidades.csv"


def cadastrar_especialidade(especialidade):
    if len(especialidade) == 0:
        return "Informe um valor"
    
    with open(caminho_tabela_especialidades, "a", newline= "") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([especialidade])
        