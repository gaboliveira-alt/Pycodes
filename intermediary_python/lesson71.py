
x, y, *garbage = (1, 2, 3, 4)


def sum_numbers(*args):
    total = 0
    for number in args:
        print('Total', total, number)
        total += number
        print('Total', total)
    print(total)



sum_numbers(1, 2, 3, 4, 5, 6)




def sum_numbers_01(*args):
    total = 0
    for number in args:
        print('Total', total, number)
        total += number
        print('Total', total)
    return total


sum_1_2_3 = sum_numbers_01(1, 2, 3)
print(sum_1_2_3)

sum_4_5_6 = sum_numbers_01(4, 5, 6)
print(sum_4_5_6)

numbers = (1, 2, 3, 4, 5, 6, 7, 78, 10)
other_sum = sum_numbers_01(*numbers)
print(other_sum)

print(sum(numbers))
print(*numbers)