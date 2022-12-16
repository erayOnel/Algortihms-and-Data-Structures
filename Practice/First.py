#from car import Car

#car_1=Car("Chevy","Corvette",2025,"Red")
#car_2=Car("Ford","Mustang",2089,"Yellow")

#print(car_1.make)
#print(car_1.model)
#print(car_1.year)
#print(car_1.color)

#Car.wheel=2
#car_1.wheel=3

#modüller içinde tanımlanan değerler müdahale edilmedikçe
#(ihtiyaç duyulduğunda) default haldedirler

#print(car_1.wheel)
#print(car_2.wheel)

#car_1.stop()
#car_2.drive()

#class Animal:
#    alive =True
#    def eat(self):
#        print("This animal is eating")
#    def sleep(self):
 #       print("This animal is sleeping")

#class Rabbit(Animal):
#parantez içinde belirtilen 'class' değeri parent classdır#
 #   def run(self):
  #      print("This rabbit is running")
#class Fish(Animal):
 #   def swim(self):
  #      print("This fish is swimming")
#class Hawk(Animal):
 #   def fly(self):
  #      print("This hawk is flying")

#rabbit=Rabbit()
#hawk=Hawk()
#fish=Fish()

#fish.eat()
#rabbit.sleep()

#class Organism:
  #  alive=True

#class Animal(Organism):
 #   def eat(self):
  #      print("This one is eating")

#class Dog(Animal):
 #   def bark(self):
  #      print("This one's barking")

#Dog().bark()
#Animal().eat()

#class Prey:
 #   def flee(self):
  #      print("This animal is flees")

#class Predator:
 #   def hunting(self):
  #      print("This one is hunting")

#class Rabbit(Prey,Predator):
 #   pass
#class Hawk(Prey):
 #   pass

#hawk=Hawk()
#rabbit=Rabbit()

#rabbit.hunting()
#rabbit.flee()


#thrift_shop=[("short",50),
         #    ("pants",20),
      #       ("jacket",30),
   #          ("socks",60)]

#tur=lambda x: (x[0],x[1]*17.61)
#birinci kısıma fonksiyon ikinci kısıma parametre değeri(listemiz)#
#to_vro=lambda x: (x[0],x[1])

#nice= list(map(tur,thrift_shop))
#notnice=list(map(to_vro,thrift_shop))
#for h in nice:
   # print(h)

#for l in notnice:
#    print(l)

            













