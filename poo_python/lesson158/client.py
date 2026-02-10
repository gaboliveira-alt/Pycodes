
from person import Person
from accounts import Account


class Client(Person):
    def __init__(self, name: str, age: int, type_account: Account):
        super().__init__(name, age)
        self.type_account: Account = type_account