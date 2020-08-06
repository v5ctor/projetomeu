import pytest

from projetomeu.spam import Enviador, EmailInvalido


def test_criar_enviador():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente', ['renat.mello,bit@gmail.com', 'victorbitt00@gmail'])

def test_remetente(remetente):
    enviador=Enviador()
    resultado=enviador.enviar(remetente,
                    'monicaremudo@yahoo.com.br',
                    'Festa Junina',
                    'Parabéns pela festa.'
                    )
    assert remetente in resultado


@pytest.mark.parametrize('remetente', ['', 'victorbittgmail'])

def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(remetente,
                             'monicaremudo@yahoo.com.br',
                            'Festa Junina',
                            'Parabéns pela festa.'
                            )
