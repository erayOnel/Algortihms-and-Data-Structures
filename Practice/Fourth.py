#class Car:

    #wheel=4

   # def __init__(self,make,model,year,color):
  #      self.make=make
 #       self.model=model
#        self.year=year
   #     self.color=color
#__init__ fonksiyonu bir sınıf için tanımlanan kodlar arasından ilk çalışan fonksiyondur,
    #içerisine değer alabileceğini belirtir

  #  def drive(self):
   #     print("This "+self.model+" is driving")
  #  def stop(self):
 #       print("This one stopped")

#    def turn_on(self):
 #       print("Nice car")
  #      return self
   # def drive(self):
    #    print("This one is driving")
     #   return self
#    def brake(self):
 #       print("This car stopped")
  #      return self
   # def turn_off(self):
    #    print("You broke the engine")
     #   return self
#Car().turn_on().drive().brake().turn_off()

#zincirleme fonksiyonlar için 'return' komutunu unutma#

#class Car:

 #   color=None

#class Motorcycle:

 #   color=None

#def change_color(vehicle,color):

 #   vehicle.color=color

#car_1=Car()
#car_2=Car()
#car_3=Car()
#bike_1=Motorcycle()
#bike_2=Motorcycle()

#change_color(car_1,"red")
#change_color(car_2,"blue")
#change_color(car_3,"yellow")
#change_color(bike_1,"magenta")
#change_color(bike_2,"cyan")

#print(car_1.color)
#print(car_2.color)
#print(car_3.color)
#print(bike_1.color)
#print(bike_2.color)

#class Duck:

 #   def walk(self):
  #      print("This duck is walking")

   # def talk(self):
    #    print("This duck is qwuacking")

#class Chicken:

 #   def walk(self):
  #      print("The chicken is walking")

   # def talk(self):
    #    print("This chick is talking")

#class Person:

 #   def catch(self,duck):
  #      duck.walk()
   #     duck.talk()
    #    print("You caught the what")


#person=Person()
#duck=Duck()
#chicken=Chicken()

#person.catch(duck)


#people=[("rachael",20),
 #       ("john",22),
  #      ("violet",25),
   #     ("ares",16),
    #    ("jess",18),
     #   ("lester",15)]

#ages=lambda data:data[1]>=18

#can_drink=list(filter(ages,people))

#'filter' komutu fonksiyon da belirtilen koşulu sağlayan değerleri alır#

#print(can_drink)

#for s in can_drink:
 #   print(s)

#import functools

#letters=["C","O","M","E","W","I","T","H","M","E"]


#learnable=functools.reduce(lambda x,y:x+y,letters)
#print(learnable)


#for_factorial=[5,4,3,2,1]
#matht=functools.reduce(lambda z,t:z*t,for_factorial)
#print(matht)


#notes=[30,40,50,60,70,80]
#passed_ones= [z for z in notes if z>=50]
#print(passed_ones)

#notes_again=[30,40,50,60,70,80,90]
#unserstand=[q if q>50 else "FAIL" for q in notes_again]
#print(unserstand)

#points=[38,41,535,679,70,234,123]
#for_points=[z if z==535 else "Damn" for z in points ]
#print(for_points)

#squares=[]
#for m in range(1,10+1):
 #   squares.append(m*m)
#print(squares)

#squares=[f * f for f in range(1,10+1) ]
#print(squares)






