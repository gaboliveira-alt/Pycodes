
class A:
    pass

    def who_i_am(self):
        print('Aqui é o A')


class B(A):
    pass
    
    #def who_i_am(self):
    #    print('Aqui é o B')


class C(A):
    pass
    
    def who_i_am(self):
        print('Aqui é o C')


class D(B, C):
    pass
    
    def who_i_am(self):
        print('Aqui é o D')


example_d = D()
example_d.who_i_am()
print(example_d.__mro__)
print(example_d.mro())