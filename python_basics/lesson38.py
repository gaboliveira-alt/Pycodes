qty_lines = 5
qty_collums = 5

line = 1

while line < qty_lines:
    collum = 1
    
    while collum < qty_collums:
        collum += 1
        print(f'{line=} {collum=}')
    
    line += 1

print('ACABOU')