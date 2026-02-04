
from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, name):
        print(name, 'está chamando', self.phone)
        return 2134


example_call = CallMe('8676755457')
example_return = example_call('Gabriel Pinto')
print(example_call)