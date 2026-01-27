from log import LogFileMixin

class Eletronic:
    def __init__(self, name):
        self._name = name
        self._connected = False
    
    def turn_on(self):
        if not self._connected:
            self._connected = True
    
    def turn_off(self):
        if self._connected:
            self._connected = False


class Smarthphone(Eletronic, LogFileMixin):
    def turn_on(self):
        super().turn_on()
        
        if self._connected:
            formated_message = f'{self._name} está ligado!'
            self.log_success(formated_message)
    
    def turn_off(self):
        super().turn_off()
        
        if not self._connected:
            formated_message = f'{self._name} está desligado!'
            self.log_error(formated_message)
