class Email:
    def enviar(self):
        return "enviando email"

class SMS:
    def enviar(self):
        return "enviado o sms"

class Pushnotificacao:
    def enviar(self):
        return "Enviando notificacao"

n = [Email(),  SMS(), Pushnotificacao()]
for notificacoes in  n:
    print(notificacoes.enviar())