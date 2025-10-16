from lesson127_a import PATH_FILE, Person
import json


with open(PATH_FILE, 'r', encoding='UTF-8') as class_file:
    data_class = json.load(class_file)
    person_01 = Person(**data_class[0])
    person_02 = Person(**data_class[1])
    person_03 = Person(**data_class[2])
    
    print(person_01.name, person_01.age)
    print(person_02.name, person_02.age)
    print(person_03.name, person_03.age)
    
    
    