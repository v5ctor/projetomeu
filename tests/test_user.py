import pytest

from projetomeu.db import Conexao
from projetomeu.modelos import Usuario


@pytest.fixture(scope='session')
def conexao():
    conexao_obj = Conexao()
    yield conexao_obj
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_user(sessao):
    usuario = Usuario(nome='Jonas')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_user(sessao):
    usuarios = [Usuario(nome='Jonas'), Usuario(nome='Mikkel')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
