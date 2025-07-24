
x = 1

def scope():
    global x
    x = 10
    def other_function():
        global x
        x = 11
        y = 2
        print(x, y)
    
    other_function()
    print(x)


print(x)
scope()
print(x)
