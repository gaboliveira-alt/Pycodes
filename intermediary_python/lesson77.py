
questions = [
    {
        'Question': 'Quanto é 2 + 2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    
    
    {
        'Question': 'Quanto é 5 x 5?',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    
    
    {
        'Question': 'Quanto é 10/2?',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]


count = 0
right_answer = 0
wrong_answer = 0


while count < 3:
    
    print(questions[count]['Question'])
    print('Escolha uma Opção: ')
    print()
    
    
    for key, value in enumerate(questions[count]['Options']):
        print(f'{key}) {value}', sep=' ')
    
    
    user_request = input('Escolha uma das opções acima: ')
    
    
    
    if user_request in questions[count]['Options']:
        if user_request != questions[count]['Answer']:
            print('Errou!\n')
            wrong_answer += 1
            count += 1
        else:
            print('Acertou!\n')
            right_answer += 1
            count += 1
    else:
        print('Isso não é uma opção valida.')
        break
    print()
    
    
    if count == 3:
        if right_answer <= 3:
            print(f'Você acertou {right_answer} de {len(questions)} questões!')
        print(f'Você errou {wrong_answer} de {len(questions)} questôes!')