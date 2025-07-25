from flask import Flask

from routes.router import (
    home_blue_print, 
    cadastro_especialidade_blue_print, 
    cadastro_horarios_blue_print, 
    listar_especialidades_blue_print,
    deletar_especialidade_blue_print,
    atualizar_especialidade_blue_print,
    atualizar_especialidade_form_blue_print
    )

from routes.medicosRouter import (
    cadastro_medicos_blue_print,
    listagem_medicos_blue_print,
    edicao_medicos_blue_print,
    excluir_medico_blue_print
)

app = Flask(__name__)
app.register_blueprint(home_blue_print)
app.register_blueprint(cadastro_especialidade_blue_print)
app.register_blueprint(cadastro_medicos_blue_print)
app.register_blueprint(cadastro_horarios_blue_print)
app.register_blueprint(listar_especialidades_blue_print)
app.register_blueprint(deletar_especialidade_blue_print)
app.register_blueprint(atualizar_especialidade_blue_print)
app.register_blueprint(atualizar_especialidade_form_blue_print)
app.register_blueprint(listagem_medicos_blue_print)
app.register_blueprint(edicao_medicos_blue_print)
app.register_blueprint(excluir_medico_blue_print)

if __name__ == "__main__":
    app.run()