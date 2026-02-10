
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, agency: int, account_number: int, balance: float = 0) -> None:
        self.agency = agency
        self.account_number = account_number
        self.balance = balance       
    
    @abstractmethod
    def withdraw(self, value: float) -> float:
        ...
    

    def deposit(self, value: float) -> float:
        if not isinstance(value, float) or value <= 0:
            raise ValueError('O deposito aceita apenas numeros e valores acimas de 0')
        self.balance += value
        self.details(f'DEPOSITO -> {self.balance}')
        return self.balance
    
    
    def details(self, msg: str = '') -> None:
        print(f'O seu saldo é {self.balance:.2f} ({msg})')
        print('----')
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agency!r} {self.account_number!r} {self.balance:.2f}'
        return f'{class_name} {attrs}'
        


class CurrentAccount(Account):
    def __init__(self, agency, account_number, balance, limit: float = 0) -> None:
        super().__init__(agency, account_number, balance)
        self._limit = limit
    
    def withdraw(self, value) -> float:
        if not isinstance(value, float):
            raise TypeError('o sacar aceita apenas digitos para sacar seu dinheiro')
        
        withdraw_value = self.balance - value
        maximum_limit = -self._limit
        
        if withdraw_value >= maximum_limit:
            self.balance -= value
            self.details(f'SAQUE {value}')
            return self.balance
        
        print('Não foi possivel realizar o seu saque')
        print(f'Seu limite atual é {-self._limit:.2f}')
        self.details(f'SAQUE NEGADO {value}')       
        return self.balance 
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agency!r} {self.account_number!r} {self.balance:.2f} {self._limit:.2f}'
        return f'{class_name} {attrs}'


class SavingsAccount(Account):
    def __init__(self, agency, account_number, balance):
        super().__init__(agency, account_number, balance)
    
    def withdraw(self, value) -> float:
        withdraw_value = self.balance - value
        
        if not isinstance(value, float) or withdraw_value < 0:
            raise ValueError('Não foi possivel realizar o seu saque com o valor desejado')
        self.balance -= value
        self.details(f'SAQUE {value}')
        return self.balance


if __name__ == '__main__':
    account = CurrentAccount(1234, 4567, 0, 100)
    account.withdraw(100.0)
    account.withdraw(140.0)
    account.deposit(100.0)
    