# -*-coding: utf-8 -*-
from datetime import datetime
from fakepay.utils import random_alphanumeric
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

FORMAS_PAGAMENTO = ['BOLETO', 'CARTAO', 'PIX']


class SolicitacaoPagamento:
    """Classe que representa uma solicitação de pagamento"""

    def __init__(self, codigo_servico: str,
                 nome_contribuinte: str,
                 valor_principal: float,
                 valor_descontos: float = 0.0,
                 valor_juros: float = 0.0,
                 valor_multa: float = 0.0,
                 valor_outros_acrescimos: float = 0.0,
                 valor_outras_deducoes: float = 0.0) -> None:
        self.codigo_servico = codigo_servico
        self.nome_contribuinte = nome_contribuinte
        self.valor_principal = valor_principal
        self.valor_descontos = valor_descontos
        self.valor_juros = valor_juros
        self.valor_multa = valor_multa
        self.valor_outros_acrescimos = valor_outros_acrescimos
        self.valor_outras_deducoes = valor_outras_deducoes
        self.vencimento = None
        self.competencia = None
        self.cnpj_cpf = None

    def total(self) -> float:
        acrescimos = self.valor_juros + self.valor_multa + self.valor_outros_acrescimos
        descontos = self.valor_descontos - self.valor_outras_deducoes
        return self.valor_principal + acrescimos - descontos


class Pagamento:
    """Classe que representa um pagamento registrado"""

    def __init__(self, valor: float, url_pagamento: str,
                 data_criacao: datetime = datetime.now(),
                 _id: str = random_alphanumeric(22)) -> None:
        self.valor = valor
        self.url_pagamento = url_pagamento
        self._id = _id
        self.data_criacao = data_criacao
        self.data_atualizacao = data_criacao
        self.id_transacao = None
        self.servico_pagamento = None
        self.situacao = 'CRIADO'

    def concluir(self):
        self.data_atualizacao = datetime.now()
        self.situacao = 'CONCLUIDO'

    def cancelar(self):
        self.data_atualizacao = datetime.now()
        self.situacao = 'CANCELADO'

    def iniciar(self):
        self.data_atualizacao = datetime.now()
        self.situacao = 'INICIADO'

    def submeter(self):
        self.data_atualizacao = datetime.now()
        self.situacao = 'SUBMETIDO'

    def rejeitar(self):
        self.data_atualizacao = datetime.now()
        self.situacao = 'REJEITADO'

    def __dict__(self):
        obj = {
            'id': self._id,
            'dataCriacao': self.data_criacao.strftime(DATETIME_FORMAT),
            'urlPagamento': self.url_pagamento,
            'situacao': self.situacao
        }

        if self.data_atualizacao:
            obj['dataAtualizacao'] = self.data_atualizacao.strftime(
                DATETIME_FORMAT)

        if self.id_transacao:
            obj['idTransacao'] = self.id_transacao

        if self.servico_pagamento:
            obj['servicoPagamento'] = self.servico_pagamento

        return obj

    @property
    def id(self):
        return self._id


class RepositorioPagamentos:
    """
    Objeto de acesso aos pagamentos registrados
    """

    def __init__(self, db):
        self.db = db

    def salvar(self, pagamento: Pagamento) -> None:
        stmt = self.db.cursor()
        sql = "INSERT INTO pagamentos(id, data_criacao, data_atualizacao, valor, situacao) VALUES (%s, %s, %s, %s, %s)"
        stmt.execute(sql, (pagamento.id,
                           pagamento.data_criacao.strftime(DATETIME_FORMAT),
                           pagamento.data_atualizacao.strftime(
                               DATETIME_FORMAT),
                           "{:.2f}".format(pagamento.valor), pagamento.situacao))
        self.db.commit()
        stmt.close()

    def atualizar(self, pagamento: Pagamento) -> None:
        stmt = self.db.cursor()
        sql = "UPDATE pagamentos SET data_criacao = %s, data_atualizacao = %s, valor = %s, situacao = %s WHERE id = %s"
        stmt.execute(sql, (pagamento.data_criacao.strftime(DATETIME_FORMAT),
                           pagamento.data_atualizacao.strftime(
                               DATETIME_FORMAT),
                           "{:.2f}".format(pagamento.valor),
                           pagamento.situacao,
                           pagamento.id))
        self.db.commit()
        stmt.close()

    def buscar_por_id(self, id_pagamento: str):
        stmt = self.db.cursor()
        sql = "SELECT id, data_criacao, data_atualizacao, valor, situacao, id_transacao, servico_pagamento " \
              "FROM pagamentos WHERE id = %s"
        stmt.execute(sql, (id_pagamento,))
        row = stmt.fetchone()

        pagamento = self.db_row_to_pagamento(row)

        stmt.close()
        return pagamento

    def db_row_to_pagamento(self, row):
        if not row:
            return None
        pagamento = Pagamento(valor=float(row[3]),
                              url_pagamento="",
                              data_criacao=datetime.fromisoformat(str(row[1])),
                              _id=row[0])
        pagamento.data_atualizacao = datetime.fromisoformat(str(row[2]))
        pagamento.situacao = row[4]
        pagamento.id_transacao = row[5]
        pagamento.servico_pagamento = row[6]
        return pagamento
