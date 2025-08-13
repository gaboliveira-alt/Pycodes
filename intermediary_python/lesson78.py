
s1 = set('Luiz')
s2 = set()
s3 = {'Luiz', 1, 3, 4, 5}

s4 = {1, 2, 3, 3, 3, 4, 5, 5}
s5 = {1, 2, 3, 4, (123,)}
print(4 in s4)
print(3 in s4)
print(2 in s4)
print(6 in s4)
print(3 not in s4)

l1 = [1, 2, 3, 3, 3, 4, 5, 5]
s6 = set(l1)
print(s6)


s7 = set()
s7.add(1)
s7.add('Gabriel')
s7.update(('Hello World', 1, 2, 3, 4, 5))
s7.discard('Gabriel')
s7.discard(1)
# s7.clear()


s8 = {1, 2, 3}
s9 = {2, 3, 4}
example_union = s8 | s9
example_intersection = s8 & s9
example_difference = s8 - s9
example_symetric_difference = s8 ^ s9
print(example_union)
print(example_intersection)
print(example_difference)
print(example_symetric_difference)