name = 'Gabriel Oliveira'
len_name = len(name)
count = 0
new_string = ''
len_new_string = len(new_string)

while len_new_string < len_name:
    
    while count < len_name:
        new_string += f'*{name[count]}'
        count += 1
        len_new_string += 1
        print(new_string)

"""
while count < len_name:
    char = name[count]
    new_string += f'*{char}'
    count += 1

new_string += '*'
print(new_string)
"""