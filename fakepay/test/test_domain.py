from unittest import TestCase, main
from fakepay.domain import Pagamento, SolicitacaoPagamento


class PagamentoTestCase(TestCase):
    """Testes de unidade da classe Pagamento"""
    def test_criacao_pagamento_minimo(self):
        valor_pagamento = 250.26
        url_pagamento = "https://foo.dev/pagamentos/12345"
        pagamento = Pagamento(valor=valor_pagamento, url_pagamento=url_pagamento)
        self.assertEqual(valor_pagamento, pagamento.valor)
        self.assertEqual(url_pagamento, pagamento.url_pagamento)
        self.assertIsNotNone(pagamento.data_criacao)
        self.assertEqual("CRIADO", pagamento.situacao)

    def test_conclusao_pagamento(self):
        valor_pagamento = 250.26
        url_pagamento = "https://foo.dev/pagamentos/12345"

        pagamento = Pagamento(valor=valor_pagamento, url_pagamento=url_pagamento)
        pagamento.concluir()

        self.assertIsNotNone(pagamento.data_atualizacao)
        self.assertEqual("CONCLUIDO", pagamento.situacao)

    def test_cancelamento_pagamento(self):
        valor_pagamento = 250.26
        url_pagamento = "https://foo.dev/pagamentos/12345"

        pagamento = Pagamento(valor=valor_pagamento, url_pagamento=url_pagamento)
        pagamento.cancelar()

        self.assertIsNotNone(pagamento.data_atualizacao)
        self.assertEqual("CANCELADO", pagamento.situacao)

    def test_rejeicao_pagamento(self):
        valor_pagamento = 250.26
        url_pagamento = "https://foo.dev/pagamentos/12345"

        pagamento = Pagamento(valor=valor_pagamento, url_pagamento=url_pagamento)
        pagamento.rejeitar()

        self.assertIsNotNone(pagamento.data_atualizacao)
        self.assertEqual("REJEITADO", pagamento.situacao)

    def test_iniciacao_pagamento(self):
        valor_pagamento = 250.26
        url_pagamento = "https://foo.dev/pagamentos/12345"

        pagamento = Pagamento(valor=valor_pagamento, url_pagamento=url_pagamento)
        pagamento.iniciar()

        self.assertIsNotNone(pagamento.data_atualizacao)
        self.assertEqual("INICIADO", pagamento.situacao)

    def test_submissao_pagamento(self):
        valor_pagamento = 250.26
        url_pagamento = "https://foo.dev/pagamentos/12345"

        pagamento = Pagamento(valor=valor_pagamento, url_pagamento=url_pagamento)
        pagamento.submeter()

        self.assertIsNotNone(pagamento.data_atualizacao)
        self.assertEqual("SUBMETIDO", pagamento.situacao)


class SolicitacaoPagamentoTestCase(TestCase):
    """Testes de unidade da classe SolicitacaoPagamento"""
    def test_inicializacao_minima(self):
        valor = 125.72
        codigo_servico = "12345"
        nome_contribuinte = "Contribuinte"
        solicitacao = SolicitacaoPagamento(codigo_servico=codigo_servico, nome_contribuinte=nome_contribuinte,
                                           valor_principal=valor)

        self.assertEqual(codigo_servico, solicitacao.codigo_servico)
        self.assertEqual(nome_contribuinte, solicitacao.nome_contribuinte)
        self.assertEqual(valor, solicitacao.valor_principal)
        self.assertEqual(0.0, solicitacao.valor_multa)
        self.assertEqual(0.0, solicitacao.valor_juros)
        self.assertEqual(0.0, solicitacao.valor_descontos)
        self.assertEqual(0.0, solicitacao.valor_outros_acrescimos)
        self.assertEqual(0.0, solicitacao.valor_outras_deducoes)

    def test_calculo_total(self):
        valor = 125.72
        codigo_servico = "12345"
        nome_contribuinte = "Contribuinte"
        solicitacao = SolicitacaoPagamento(codigo_servico=codigo_servico, nome_contribuinte=nome_contribuinte,
                                           valor_principal=valor, valor_multa=2.53, valor_descontos=2.53)
        self.assertEqual(valor, solicitacao.total())


if __name__ == '__main__':
    main()
