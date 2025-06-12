phrase = 'Value read'

i = 0
while i < len(phrase):
    char = phrase[i]
    
    if char == ' ':
        break
    
    print(char)
    i += 1
else:
    print('Não tem espaço na string')
print('Fora do While')
