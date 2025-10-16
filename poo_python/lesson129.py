
class ExampleClass:
    
    @staticmethod
    def function_class(*args, **kwargs):
        print('Oi', args, kwargs)


def example_function(*args, **kwargs):
    print('Oi', args, kwargs)


c1 = ExampleClass()
c1.function_class('nada aqui', nomeado='receba')
example_function(1, 2, 4)
ExampleClass.function_class(1, 2, 3, 4, 5)
example_function(nomeado=2)
