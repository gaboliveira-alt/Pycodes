import os


trys_user = ''
secret_word = 'python'
count = 0

while True:
    
    input_user = input('Digite uma palavra: ').lower()
    count += 1

    
    if len(input_user) > 1:
        print('Digite apenas uma palavra')
        continue
    
    
    if input_user in secret_word:
        trys_user += input_user
    
    
    revelead_word = '' 
    for actual_phrase in secret_word:
        if actual_phrase in trys_user:
            revelead_word += actual_phrase
        else:
            revelead_word += '*'
    print(revelead_word)
    
    
    if revelead_word == secret_word:
        os.system('cls')
        print('Parabens voce descobriu!')
        print('A Palavra secreta era:', secret_word)
        print('Tentativas:', count)
        trys_user = ''
        revelead_word = ''
        continue