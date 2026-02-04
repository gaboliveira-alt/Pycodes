
from contextlib import contextmanager

@contextmanager
def my_open(path_file, file_mode):
    file = None
    try:
        print('Abrindo Arquivo')
        file = open(path_file, file_mode, encoding='utf8')
        yield file
    except Exception as e:
        print('Ocorreu erro', e)
    finally:
        print('Fechando o Arquivo')
        if file is not None:
            file.close()


with my_open('lesson150.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    print('WITH', file)