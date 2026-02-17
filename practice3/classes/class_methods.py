# 1
class Person:
    species = "Human"

    @classmethod
    def get_species(cls):
        return cls.species


# 2
class Math:
    @classmethod
    def add(cls, a, b):
        return a + b


# 3
class Counter:
    count = 0

    @classmethod
    def increase(cls):
        cls.count += 1


# 4
class School:
    name = "ABC School"

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name
