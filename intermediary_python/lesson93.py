
try:
    a = 18
    b = 0
    #print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Variavel b não foi definida')
except (TypeError, IndexError) as error:
    print('MSG:', error)
    print('NAME:', error.__class__.__name__)
except Exception:
    print('Erro DESCONHECIDO')


print('FINAL DO CODIGO')