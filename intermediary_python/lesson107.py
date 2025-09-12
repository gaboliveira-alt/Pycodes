from itertools import zip_longest


def initial_zipper(list_city, list_state):
    city_state = [
        (list_city[count], list_state[count])
        for count in range(len(list_city))
    ]
    return city_state


def zipper(list_city, list_state):
    minumun_range = min(len(list_city), len(list_state))
    
    city_states = [
        (list_city[index], list_state[index]) 
        for index in range(minumun_range)
    ]
    return city_states


citys = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA', 'SP', 'MG', 'RJ']
first_zipped_list = initial_zipper(citys, states)
zipped_list = zipper(citys, states)
print(*first_zipped_list, sep=', ')
print(*zipped_list, sep=', ')
print(list(zip(citys, states)))
print(list(zip_longest(citys, states, fillvalue='Cidade Descionhecida')))