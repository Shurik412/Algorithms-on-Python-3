"""
namedtuple - именованный кортеж, обеспечивающий доступ к содержимому по именам.
"""
from collections import namedtuple

hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_1[4])


class Person:
    def __init__(self, name, race, health, mana, strength):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.strength = strength


hero_2 = Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_2.mana)

New_Person = namedtuple('New_Person', 'name, race, health, mana, strength')
hero_3 = New_Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_3.race)

prop = ['name', 'race', 'health', '_mana', 'strength']
New_Person_1 = namedtuple('New_Person', prop, rename=True)
hero_4 = New_Person_1('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_4.race)

print('*' * 50)
Point = namedtuple('Point', 'x, y, z')
p1 = Point(2, z=3, y=4)
print(p1)

t = [5, 10, 15]
p2 = Point._make(t)
print(p2)

d2 = p2._asdict()
print(d2)

# p2.x = 6
p3 = p2._replace(x=6)
print(p3)

print(p3._fields)

print('*' * 10)
New_Point = namedtuple("New_Person", 'x,y,z', defaults=[0, 0])
p4 = New_Point(5)
print(p4)

print(p4._field_defaults)

dct = {'x': 10, 'y': 20, 'z': 30}
p5 = New_Point(**dct)
print(p5)