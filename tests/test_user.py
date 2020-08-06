from projetomeu.db import Conexao
from projetomeu.modelos import Usuario


def test_salvar_user():
    conexao = Conexao()
    sessao= conexao.gerar_sessao()
    usuario = Usuario(nome='Jonas')
    sessao.salvar(usuario)
    assert isinstance(usuario.id,int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()

def test_listar_user():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Jonas'), Usuario(nome='Mikkel')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()