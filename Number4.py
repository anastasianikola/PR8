class Nikola:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        if name != "Николай":
            self.name = f"Я не {name}, а Николай"
        else:
            self.name = name
        self.age = age

person1 = Nikola("Максим", 25)
print(person1.name)
print(person1.age)