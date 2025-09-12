from itertools import zip_longest


def sum_lists(number_list01, number_list02):
    minimum_range = min(len(number_list02), len(number_list01))
    
    sum_list = [
        number_list01[index] + number_list02[index]
        for index in range(minimum_range)
    ]
    return sum_list


numbers_list01 = [1, 2, 3, 4, 5, 6]
numbers_list02 = [1, 2, 3, 4]
sum_list = []
sum_list02 = []
sum_list03 = [n1 + n2 for n1, n2 in zip(numbers_list01, numbers_list02)]
sum_list04 = [n1 + n2 for n1, n2 in zip_longest(numbers_list01, numbers_list02, fillvalue=0)]

for i in range(len(numbers_list02)):
    sum_list.append(numbers_list01[i] + numbers_list02[i])


for i, _ in enumerate(numbers_list02):
    sum_list02.append(numbers_list01[i] + numbers_list02[i])


sum_list05 = sum_lists(numbers_list01, numbers_list02)
print(sum_list)
print(sum_list02)
print(sum_list03)
print(sum_list04)
print(sum_list05)