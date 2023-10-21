class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


class ChildDog(Dog):

    def __init__(self, name, age):
        super().__init__("Child" + name, age)
        self.new_fac = "abc"

    def child_method(self):
        print(f"{self.name} age is {self.age}")

    def roll_over(self):
        print(f"{self.name} age is {self.age} new fac is {self.new_fac}")


mydog = Dog("zss", 12)
mydog.sit()
mydog.roll_over()
mydog.name = "list"
mydog.roll_over()
my_child_dog = ChildDog("xxx", 11)
my_child_dog.child_method()
my_child_dog.roll_over()
