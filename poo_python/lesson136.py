
class Client:
    def __init__(self, name):
        self.name = name
        self.addresses = []
    
    def insert_address(self, street, number):
        self.addresses.append(Address(street, number))
    
    def insert_external_address(self, address):
        self.addresses.append(address)
    
    def show_addresses(self):
        for address in self.addresses:
            print(address.street, address.number)
    
    def __del__(self):
        print('APAGANDO', self.name)


class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number
    
    def __del__(self):
        print('APAGANDO', self.street, self.number)


client01 = Client('Fabricio')

client01.insert_address('Av Darth Revan', 1234)
client01.insert_address('Av Darth Vader', 3456)
external_address = Address('Av Darth Sidious', 5678)
client01.insert_external_address(external_address)
client01.show_addresses()

del client01

print(external_address.street, external_address.number)
print('MEU CODIGO ACABA AQUI NESSA LINHA 37')