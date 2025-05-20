counter = 0

while counter <= 100:
    counter += 1
    
    
    if counter == 6:
        print('Não vou mostrar o 6')
        continue
    
    
    if counter >= 10 and counter <= 27:
        print('Não vou mostrar o', counter)
        continue
    
    if counter == 50:
        break


print('ACABOU')

