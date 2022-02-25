from fakepay.domain import SolicitacaoPagamento, Pagamento, RepositorioPagamentos


class SolicitarPagamento:
    """
    Caso de uso de solicitação de pagamento
    """

    def __init__(self, repositorio: RepositorioPagamentos):
        self.repositorio = repositorio

    def executar(self, solicitacao) -> Pagamento:
        pagamento = Pagamento(valor=solicitacao.total(), url_pagamento="")
        pagamento.url_pagamento = "/pagar/%s" % (pagamento._id)
        self.repositorio.salvar(pagamento)
        return pagamento


class AtualizarPagamento:
    def __init__(self):
        # TODO Implementar
        pass


class ExecutarPagamento:
    """
    Executa pagamento de uma solicitação de pagamento
    """

    def __init__(self, repositorio: RepositorioPagamentos):
        self.repositorio = repositorio

    def executar(self, pagamento: Pagamento) -> bool:
        pagamento.concluir()
        self.repositorio.atualizar(pagamento)
