name = 'Gabriel Oliveira Pinto'
i = 0

while i < len(name):
    
    if name[i] == ' ':
        i += 1
        continue
    
    
    print(name[i], i)
    i += 1

"""
saved_password = '12345'
try_password = ''
counter = 0

while saved_password != try_password:
    try_password = input(f'Sua senha ({counter})x: ')
    
    counter += 1
"""    

text = 'Python'
new_text = ''

for char in text:
    new_text += f'*{char}'
    print(char)
print(new_text)


