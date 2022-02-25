from bottle import Bottle, abort, redirect, request, response, static_file, template, view, TEMPLATE_PATH
import json
import re
import os
from fakepay.domain import FORMAS_PAGAMENTO, RepositorioPagamentos, SolicitacaoPagamento
from fakepay.usecases import SolicitarPagamento, ExecutarPagamento
from fakepay.database import DatabaseHelper

# Adiciona o caminho atual a lista de carregamento de templates
TEMPLATE_PATH.append('./fakepay/views')

db_url = os.path.realpath("./database/db.sqlite")
print("DB_URL = ", db_url)
app = Bottle()
db = DatabaseHelper(db_url=db_url)
repo = RepositorioPagamentos(db=db.connection)


@app.route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="./fakepay/static")


@app.route("/")
@view("index.tpl.html")
def index():
    pass


@app.post("/api/gru/solicitacao-pagamento")
def solicita_pagamento():
    use_case = SolicitarPagamento(repo)
    obj = request.json
    solicitacao = SolicitacaoPagamento(codigo_servico=obj['codigoServico'],
                                       nome_contribuinte=obj['nomeContribuinte'],
                                       valor_principal=float(
                                           obj['valorPrincipal']),
                                       valor_descontos=float(
                                           obj['valorDescontos']),
                                       valor_juros=float(obj['valorJuros']),
                                       valor_multa=float(obj['valorMulta']),
                                       valor_outras_deducoes=float(
                                           obj['valorOutrasDeducoes']),
                                       valor_outros_acrescimos=float(
                                           obj['valorOutrosAcrescimos'])
                                       )
    pagamento = use_case.executar(solicitacao=solicitacao)
    pagamento.url_pagamento = re.sub(
        r"/api/.+", "", request.url) + pagamento.url_pagamento
    if pagamento is None:
        response.status = 404
        return

    response.status = 201
    response.headers['Location'] = '/api/pagamentos/%s' % (pagamento._id)
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(pagamento.__dict__())


@app.get("/pagar/:id")
def pagina_pagamento(id: str):
    pagamento = repo.buscar_por_id(id)
    if pagamento == None:
        abort(404, "Pagamento não encontrado")
        return

    return template('pagamento.tpl.html', {'pagamento': pagamento})


@app.post("/pagar/:id")
def executar_pagamento(id: str):
    pagamento = repo.buscar_por_id(id)
    if pagamento == None:
        abort(404, "Pagamento não encontrado")
        return

    forma_pagamento = request.forms['formapagamento']
    if forma_pagamento not in FORMAS_PAGAMENTO:
        redirect(request.url)
        return

    use_case = ExecutarPagamento(repo)
    use_case.executar(pagamento)

    return template('pagamento.tpl.html', {'pagamento': pagamento, 'message': 'Pagamento realizado com sucesso!'})


@app.error(404)
@view("404.tpl.html")
def not_found(error):
    return {}
