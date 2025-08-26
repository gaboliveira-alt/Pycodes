
string = 'gabriel'
method_str = 'upper'

if hasattr(string, method_str):
    print('Esse é o upper!')
    print(getattr(string, method_str)())
else:
    print(f'Não existe esse metodo {method_str}')