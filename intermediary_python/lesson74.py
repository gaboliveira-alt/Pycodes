
def create_saudation(saudation):
    def say_saudation(name):
        return f'{saudation}, {name}'
    return say_saudation


say_good_morning = create_saudation('Bom dia')
say_good_evening = create_saudation('Boa noite')

print(say_good_morning('Gabriel'))
print(say_good_evening('Mariana'))

say_good_morning_1 = create_saudation('Bom dia')
say_good_evening_1 = create_saudation('Boa noite')


for name in ['Francisco', 'Ruan', 'Denis']:
    print(say_good_evening_1(name))
    print(say_good_morning_1(name))