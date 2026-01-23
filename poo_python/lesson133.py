from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é publico guys'
        self._protected = 'isso é protegido guys'
        self.__private = 'isso aqui é privado guys'
    
    def method_public(self):
        print('metodo_publico')
        self.__method_private()
        self._method_protected()
        return 'method public guys'
    
    def _method_protected(self):
        print('_metodo_protegido')
        return '_method_protected'
    
    def __method_private(self):
        print('__metodo_privado')
        return '__method_private'
    

fi_fa = Foo()
print(fi_fa.method_public())