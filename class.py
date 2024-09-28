# Defining the Person class
class Person:
    # Constructor method to initialize attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Method to introduce the person
    def introduce(self):
        print(f"Hello! My name is {self.name}. I am {self.age} years old, and I am {self.gender}.")

# Creating an instance of the Person class
person1 = Person("Alice", 30, "female")

# Calling the introduce method to display the person's information
person1.introduce()
