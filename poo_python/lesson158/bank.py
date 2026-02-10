
from client import Client
from my_error import raise_agency, raise_client, raise_account

class Bank:
    def __init__(self, name: str, bank_agency: int) -> None:
        self.name = name
        self.bank_agency = bank_agency
        self._clients: list[Client] = []
    
    def add_clients(self, *args: Client):
        self._clients.append(*args)
    
    def verify_agency(self, client_account: Client):
        if client_account.type_account.agency == self.bank_agency:
            print(f'{self.name} - contém esta conta com essa agencia ({client_account.type_account.agency})')
            return
        raise_agency()
    
    def verfiy_client(self, client_account: Client):
        for client in self._clients:
            if client is client_account:
                print(f'{self.name} - contém este cliente ({client_account.person_name})')
                return
        raise_client()
    
    def verify_account(self, client_account: Client):
        for client in self._clients:
            if client.type_account.__class__.__name__ == client_account.type_account.__class__.__name__:
                print(f'{self.name} - contém esta conta deste cliente ({client_account.person_name}) - {client_account.type_account}')
                return
        raise_account()
