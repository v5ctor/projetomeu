import pytest

from projetomeu.main import EnviadorSpam
from projetomeu.modelos import Usuario
from projetomeu.spam import Enviador


class EnviadorMock(Enviador):
    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_envio = (remetente, destinatario, assunto, corpo)


@pytest.mark.parametrize(
    'usuarios', [[Usuario(nome='Víctor', email='victorbitt00@gmail.com'),
                  Usuario(nome='Mikkel', email='mikkanwhald@nielsen.com')],
                 [Usuario(nome='Víctor', email='victorbitt00@gmail.com')
                  ]
                 ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_spam = EnviadorSpam(sessao, enviador)
    enviador_spam.enviar_emails('victorbitt00@gmail.com',
                                'Currículo',
                                'Segue análise do seu currículo')
    assert len(usuarios) == enviador.qtd_enviados


def test_parametros_spam(sessao, usuario):
    Usuario(nome='Víctor', email='victorbitt00@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_spam = EnviadorSpam(sessao, enviador)
    enviador_spam.enviar_emails('mikkanwhald@nielsen.com',
                                'Currículo',
                                'Segue análise do seu currículo')
    assert enviador.parametros_envio == ('mikkanwhald@nielsen.com',
                                         'victorbitt00@gmail.com',
                                         'Currículo',
                                         'Segue análise do seu currículo')
