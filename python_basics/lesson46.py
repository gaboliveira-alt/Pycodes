
for i in range(10):
    
    if i == 2:
        print('Seu i é 2, pulando...')
        continue
    
    
    if i == 8:
        print("Seu i é 8, seu else não será executado")
        continue
    
    
    for j in range(1, 3):
        print(i, j)
        
else:
    print("For completo com sucesso!")