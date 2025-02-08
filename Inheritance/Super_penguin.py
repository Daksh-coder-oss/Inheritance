#Write a program to create a base class Bird, with a constructor and two methods
# Then, create a child class that inherits the constructor from Class Bird and has two functions.
#  Finally, display how you can use Super to access the parent class constructor inside the child class.

class Bird:
    def __init__(self):
        print("Bird is ready to fly")
    def question1(self):
        print("Who are you?")
    def question2(self):
        print("Can you fly")
class Parrot(Bird):
    def __init__(self):
        print("This is parrot")
        super().__init__()
    def question3(self):
        print("How are you?")
    def question4(self):
        print("What are you doing?")
obj=Parrot()
obj.question1()
obj.question2()
obj.question3()
obj.question4()

