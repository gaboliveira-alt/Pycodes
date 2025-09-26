
def add_clients(name, client_list=None):
    if client_list is None:
        client_list = []
    client_list.append(name)
    return client_list


client01 = add_clients('Gabriel')
add_clients('Fabricio', client01)
add_clients('Fernanda', client01)
client01.append('Receba')

client02 = add_clients('Helena')
add_clients('Bill', client02)

client03 = add_clients('Francisco')
add_clients('Ruan', client03)

print(client01)
print(client02)
print(client03)