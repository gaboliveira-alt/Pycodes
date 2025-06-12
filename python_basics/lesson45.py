
text = 'Gabriel'.__iter__()
text1 = iter('Gabriel')

print(text.__next__())
print(text.__next__())
print(text.__next__())
print(text.__next__())
print(text.__next__())
print(text.__next__())
print(text.__next__())
print(next(text1))

numbers = range(0, 100, 8)

for number in numbers:
    print(number)


text2 = 'Gabriel'
iterator = iter(text2)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break