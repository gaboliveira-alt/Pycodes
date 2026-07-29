import random

random.seed()

r_range = random.randrange(10, 20, 2)
print(r_range)

r_int = random.randint(10, 20)
print(r_int)

r_uniform = random.uniform(10, 30)
print(r_uniform)

names_persons = ["Luiz", "Maria", "Jõao", "David"]
random.shuffle(names_persons)
print(names_persons)

new_names = random.sample(names_persons, k=3)
print(names_persons)
print(new_names)

new_names01 = random.choices(names_persons, k=3)
print(names_persons)
print(new_names01)

print(random.choice(names_persons))
