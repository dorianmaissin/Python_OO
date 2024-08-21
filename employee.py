from class_attribute import Person
class Employee(Person):
    mounthly_salary = 0

    def annual_salary(self):
        annual_salary = 12 * self.mounthly_salary
        print(annual_salary)
    
    def is_intership(self):
        # I'm surcharging my method because I used some instance attributes from the class Person
        if self.age > 18 and self.age < 21:
            print("You are eligible for intership")
        else:
            print("You are not eligible for intership ")
    
    def is_major(self):
        if self.age <= 18:
            self.major = True
        else:
            self.major = False
        return print(self.major)


Employee1 = Employee("Dorian", 16, "14/07/1993") 
Employee1.mounthly_salary = 2000
Employee1.annual_salary()
Employee1.is_major()
