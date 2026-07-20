# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.

import os

path_example = os.path.join("Github", "Pycodes", "modules_python", "lesson168.txt")
print(path_example)

directory, file_example = os.path.split(path_example)
file_name, extension_file = os.path.splitext(file_example)
print(file_name, extension_file)
print(os.path.exists("\\Users\\kylor\\OneDrive\\Documentos\\GitHub\\Pycodes\\modules_python"))
print(os.path.abspath("."))

print(directory)
print(path_example)
print(os.path.basename(path_example))
print(os.path.basename(directory))
print(os.path.dirname(path_example))
