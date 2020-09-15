from projetomeu.modelos import Usuario


def test_salvar_user(sessao):
    usuario = Usuario(nome='Víctor', email='victorbitt00@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_user(sessao):
    usuarios = [Usuario(nome='Víctor', email='victorbitt00@gmail.com'),
                Usuario(nome='Mikkel', email='mikkanwhald@nielsen.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
