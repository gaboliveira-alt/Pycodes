
def create_multi(multiplicator):
    def multi_number(number):
        return number * multiplicator
    return multi_number


example_01 = create_multi(2)
example_02 = create_multi(3)
example_03 = create_multi(4)

print(example_01(2))
print(example_02(2))
print(example_03(2))