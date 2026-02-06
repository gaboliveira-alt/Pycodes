
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency, account_number, balance=0):
        self.agency = agency
        self.account_number = account_number
        self.balance = balance       
    
    @abstractmethod
    def withdraw(self, value):
        ...
    

    def deposit(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('O deposito aceita apenas numeros e valores acimas de 0')
        self.balance += value


class CurrentAccount(Account):
    def __init__(self, agency, account_number, balance=0):
        super().__init__(agency, account_number, balance)
    
    def withdraw(self, value):
        if not isinstance(value, int):
            raise TypeError('o sacar aceita apenas digitos para sacar seu dinheiro')
        
        if self.balance > 0 or self.balance < 0:
            self.balance -= value
            return


class SavingsAccount(Account):
    def __init__(self, agency, account_number, balance=0):
        super().__init__(agency, account_number, balance)
    
    def withdraw(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError('O sacar aceita apenas numeros e valores acimas de 0')
        
        if self.balance > 0:
            self.balance -= value
            return    