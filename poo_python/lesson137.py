
class Car:
    def __init__(self, name, type_car):
        self.name = name
        self.type_car = type_car
            

class Engine:
    def __init__(self, name):
        self.name = name
    

class ManuFacturer:
    def __init__(self, name):
        self.name = name
        self._cars = []
        self._engine = None
    
    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, type_engine):
        self._engine = type_engine
    
    def insert_cars(self, name, type_car):
        self._cars.append(Car(name, type_car))
    
    def show_profile_cars(self):
        print()
        print(f'Fabricante: {self.name}.')
        print(f'Tipo de Motor: {self.engine}.\n')
        print('-' * 15)
        
        for car in self._cars:
            print(f'Carros que contém o fabricante e o motor em comum: {car.name}, {car.type_car}.\n')


example_engine = Engine('RT9008-P')
manufacturer_example = ManuFacturer('Bora Bill')
manufacturer_example.engine = example_engine

manufacturer_example.insert_cars('Buggati', 'Super')
manufacturer_example.insert_cars('Zentorno', 'Super')
manufacturer_example.insert_cars('Type-Z', 'Super')
manufacturer_example.insert_cars('EP300', 'Super')

manufacturer_example.show_profile_cars()