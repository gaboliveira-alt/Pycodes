import json

path_file = 'C:\\Users\\kylor\\OneDrive\\Documentos\\GitHub\\Pycodes\\example_pathfile\\'
path_file += 'lesson117.json'

person = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}


with open(path_file, 'w', encoding='utf8') as json_file:
    json.dump(person, json_file, ensure_ascii=False, indent=2)


with open(path_file, 'r', encoding='utf8') as json_file:
    person = json.load(json_file)
    print(person['sobrenome'])
    