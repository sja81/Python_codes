import sys

# ha nem hasznalok __slots__ akkor a class egy Dict-be menti az osztaly atributumait key-value parosban
# ha __slots__ van hasznalva, akkor nem lehet dinamikussan letrehozni atributumokat
# pl. az u2.email="my@email.com" nem fog mukodni, mig az u1.email="" mukodni fog
class User1:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class User2:
    __slots__ = ("name", "age")

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


u1 = User1("David", 30)
u2 = User2("David", 32)

print(f"Size of object U1: {sys.getsizeof(u1.__dict__)}")
print(f"Size of object U2: {sys.getsizeof(u2.__dict__)}")


