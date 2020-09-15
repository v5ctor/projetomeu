class Enviador:
    def __init__(self):
        self.qtd_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise Email_Invalido(f'E-mail de remetente inválido: {remetente}')
        self.qtd_enviados+=1
        return remetente


class Email_Invalido (Exception):
    pass
