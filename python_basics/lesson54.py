
shopping_list = []

while True:
    print(f'Selecione uma das Opções\n')
    insert_elements = input('[i]nserir, [a]pagar, [l]istar: ').lower()
    

    if insert_elements == 'i':
        item = input('Adicione o item a seu carrinho: ')
        shopping_list.append(item)
        
        
    if insert_elements == 'a':
        removed_item = input('Selecione o numero do item a ser removido: ')
        try:
            int_removed_item = int(removed_item)
            del shopping_list[int_removed_item]
        except ValueError:
            print('Por favor digite apenas numeros.')
        except IndexError:
            print('Não existe esse numero de item no seu carrinho')
        
        
    if insert_elements == 'l':
        if len(shopping_list) > 1:
            for item_index, name in enumerate(shopping_list):
                print(item_index, name)
        else:
            print('Não há nada para listar!')