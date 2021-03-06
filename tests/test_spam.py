import pytest

from projetomeu.spam import Enviador, Email_Invalido


def test_criar_enviador():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente', ['mikkanwhald@nielsen.com', 'victorbitt00@gmail'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(remetente,
                                'monicaremudo@yahoo.com.br',
                                'Festa Junina',
                                'Parabéns pela festa.'
                                )
    assert remetente in resultado


@pytest.mark.parametrize('remetente', ['', 'victorbittgmail'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(Email_Invalido):
        enviador.enviar(remetente,
                        'monicaremudo@yahoo.com.br',
                        'Festa Junina',
                        'Parabéns pela festa.'
                        )
