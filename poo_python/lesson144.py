
from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, message) -> None:
        self.message = message
    
    @abstractmethod
    def send_message(self) -> bool:
        pass


class NotificationEmail(Notification):
    def send_message(self) -> bool:
        print(f'E-mail enviado: - {self.message}')
        return True


class NotificationSms(Notification):
    def send_message(self):
        print(f'SMS enviado: - {self.message}')
        return False


def notify(notification: Notification):
    send_notification = notification.send_message()
    
    if send_notification:
        print('Notificação enviada com sucesso!')
    else:
        print('Notificação NÃO enviada.')
        

example_notification = NotificationEmail('Testando o Email aqui tropa')
notify(example_notification)

example_notification01 = NotificationSms('Testando o SMS')
notify(example_notification01)