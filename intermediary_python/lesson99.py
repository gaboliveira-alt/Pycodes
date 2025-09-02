# from sys import path
# import lesson99_package.module
# from lesson99_package import module
# from lesson99_package.module import *
# #from lesson99_package.module import module_sum


# #print(*path, sep='\n')
# print(module_sum(2, 4))
# print(module.module_sum(2, 4))
# print(lesson99_package.module.module_sum(2, 4))
# print(module_variable)
# print(new_variable)

# from lesson99_package.module import say_hi, module_sum

# print(__name__)
# print(say_hi())

from lesson99_package.module import say_hi, module_sum

say_hi()
print(module_sum(2, 4))