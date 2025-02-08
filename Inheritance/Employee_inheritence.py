class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print("Name is:",self.name,"Id is:",self.id)
class Employee(Person):
    def __init__(self,name,id,post,salary):
        self.post=post
        self.salary=salary
        Person.__init__(self,name,id)
obj=Employee("Daksh",1245,"Manager",2000000)
obj.display()