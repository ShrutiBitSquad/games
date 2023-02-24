class Calculate:
    def add(self, a, b):
        print("a + b = {}".format(a + b))


class Adds(Calculate):
    def add(self, a, b, c = 0 ):
        print("a + b + c = {}".format(a + b + c))

c1 = Adds()
c1.add(10, 20, 30)
c1.add(10,20)

#  abstract base class work   
from abc import ABC, abstractmethod   
class Car(ABC):   
    @abstractmethod
    def mileage(self):   
        pass  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage() 
