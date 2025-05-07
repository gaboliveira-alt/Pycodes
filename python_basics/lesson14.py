a = 'A'
b = 'B'
c = 1.1
string_format = 'a={name1} b={name2} c={name3:.2f}'
format = string_format.format(name1 = a, name2 = b, name3 = c)

print(format)
