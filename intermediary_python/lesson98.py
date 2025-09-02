import importlib
import lesson98_m

print(lesson98_m.module_variable)


for i in range(10):
    importlib.reload(lesson98_m)
    print(i)

print('Fim.')