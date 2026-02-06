
import enum

class Directions(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()
    TOP = enum.auto()
    DOWN = enum.auto()


print(Directions(1), Directions['LEFT'], Directions.LEFT)
print(Directions(1).name, Directions.LEFT.value)

def move(direction: Directions):
    if not isinstance(direction, Directions):
        raise ValueError('Isso não se encaixa como uma direção')
    
    print(f'Movendo para {direction.name} ({direction.value})')

move(Directions.RIGHT)
move(Directions.LEFT)
move(Directions.TOP)
move(Directions.DOWN)