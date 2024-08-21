class Person:
    # Class Attribute
    species = "Homo sapiens"
    # Instance Attribute
    def __init__(self,name, age, anniversary):
        self.name = name
        self.age = age
        self.anniversary = anniversary
        self.major = None
    
    def is_major(self):
        if self.age >= 18:
            self.major = True
        else:
            self.major = False
        return print(self.major)
    
    def say_hello(self):
        print(f"Hello my name is {self.name}")

person1 = Person("Dorian", 31, "14/07/1993")
person2 = Person("Alice", 17, "14/07/1993")

print(person1.name)
print(person2.species)
person1.say_hello()
person2.is_major()

