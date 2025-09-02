
try:
    print('ABRIR ARQUIVO')
    #8/0
except ZeroDivisionError as error:
    print(error.__class__.__name__)
    print(error)
except IndexError:
    print('IndexError')
except (NameError, ImportError):
    print('NameError + ImportError')
else:
    print('Não deu erro nenhum')
finally:
    print('FECHOU O ARQUIVO')