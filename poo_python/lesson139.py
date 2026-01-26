
class MyString(str):
    def upper(self):
        print('CHAMOU O UPPER')
        return_supper = super().upper()
        print('DEPOIS DO UPPER SER FEITO')
        return return_supper

example_string = MyString('Bora bill')
print(example_string.upper())


class A(object):
    attribute_a = 'A'
    
    def __init__(self, attribute):
        self.attribute = attribute
    
    def method_a(self):
        print('Metodo do A')


class B(A):
    attribute_b = 'B'
    
    def __init__(self, attribute, other_thing):
        super().__init__(attribute)
        self.other_thing = other_thing
    
    def method_b(self):
        print('Metodo do B')


class C(B):
    attribute_c = 'C'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def method_c(self):
        # super().method_b 
        # super(B, self).method_b()
        # super(A, self).method_a()
        A.method_a()
        B.method_b()
        print('Metodo de C')

print(C.mro())
print(B.mro())
print(A.mro())
c = C('Atributo', 'Sei la')
print(c.attribute)
print(c.other_thing)
c.method_c()