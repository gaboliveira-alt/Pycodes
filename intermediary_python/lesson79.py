
chars = set()

while True:
    
    char = input('Digite uma letra: ')
    chars.add(char.lower())
    
    if 'l' in chars:
        print('Parabéns você achou a letra misteriosa!')
        break
    
    print(chars)