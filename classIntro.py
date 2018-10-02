class Employee:
    "This is Employee class"
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        if name is None:
            self.name = input("Enter name: ")

        self.name = name

    def set_age(self):
        try:
            self.age = int(input("Enter Age: "))
        except ValueError:
            print("Invalid Input, age must be an Integer!")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


emp1 = Employee("Abhishek", 20)

print("age:", emp1.get_age())
print("name:", emp1.get_name())

emp1.set_name("Mr. Saxena")
print("name:", emp1.get_name())

print(Employee.__doc__)
