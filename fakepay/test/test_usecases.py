import unittest
from unittest.mock import Mock
from fakepay.domain import SolicitacaoPagamento, RepositorioPagamentos
from fakepay.usecases import SolicitarPagamento


class SolicitarPagamentoTestCase(unittest.TestCase):
    """Testes de unidade da classe SolicitarPagamento"""

    def test_solicitacao_pagamento(self):
        solicitacao = SolicitacaoPagamento(codigo_servico="12345", nome_contribuinte="Contribuinte", valor_principal=125.58)
        repositorio = Mock(spec=RepositorioPagamentos)
        caso_de_uso = SolicitarPagamento(repositorio=repositorio)
        pagamento = caso_de_uso.executar(solicitacao)

        # Verifica se o repositório foi chamado para salvar o pagamento gerado
        repositorio.salvar.assert_called_once_with(pagamento)

        self.assertIsNotNone(pagamento.url_pagamento)
        self.assertEqual(pagamento.valor, solicitacao.total())


if __name__ == '__main__':
    unittest.main()
