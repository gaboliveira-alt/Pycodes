
phrase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossum'

i = 0
quantity_letter_times = 0
letter_times = ''
while i < len(phrase):
    
    actual_letter = phrase[i]
    
    
    if actual_letter == ' ':
        i += 1
        continue
    
    
    quantity_letter_actual = phrase.count(actual_letter)
    
    
    if quantity_letter_times < quantity_letter_actual:
        letter_times = actual_letter
        quantity_letter_times = quantity_letter_actual
    
    i += 1


print(
    f'A letra que apareceu mais vezes foi '
    f'"{letter_times}" que apareceu '
    f'{quantity_letter_times}x '
      )