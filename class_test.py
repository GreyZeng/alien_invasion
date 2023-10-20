class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")


mydog = Dog("zss",12)
mydog.sit()
mydog.roll_over()
mydog.name = "list"
mydog.roll_over()