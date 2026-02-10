
from client import Client
from bank import Bank
from accounts import CurrentAccount, SavingsAccount

client_1 = Client('Nome', 19, SavingsAccount(123, 4567, 0))
client_2 = Client('Nome', 19, CurrentAccount(124, 4567, 0))
bank_1 = Bank('Nubank', 123)
bank_1.add_clients(client_1)
        
bank_1.verify_agency(client_2)
bank_1.verfiy_client(client_2)
