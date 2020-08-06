class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise Email_Invalido(f'E-mail de remetente inválido: {remetente}')
        return remetente


class Email_Invalido (Exception):
    pass
