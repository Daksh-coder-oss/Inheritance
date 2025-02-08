class Vehicle:
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage
class Bus(Vehicle):
    pass
obj=Bus("Volvo",70,100)
print(obj.name,obj.speed,obj.mileage)
