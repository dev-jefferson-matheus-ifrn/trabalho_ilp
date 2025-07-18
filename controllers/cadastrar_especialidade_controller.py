from services.cadastrar_especialidade import cadastrar_especialidade

def cadastrar_especialidade_controller(requisisao):
    if requisisao.method == 'POST':
        especialidade = requisisao.form.get('especialidade')
        cadastrar_especialidade(especialidade)