
from person import Person
import accounts


class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._type_account: accounts.Account | None = None