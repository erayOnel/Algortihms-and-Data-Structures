#class Animal:

 #   def eat(self):
  #      print("This one is eating")

#class Rabbit(Animal):

 #   def eat(self):
  #      print("This rabbit s eating")
#Aynı fonksiyonlar kümenin kendisinde ve alt kümesinde bulunuyorsa (alt kümedeki) kendisine fonksiyonel olarak yakın olanı alır#

#Rabbit().eat()

#class Rectangle:
 #   def __init__(self,length,width):
 #       self.length=length
 #       self.width=width
#class Square(Rectangle):
 #   def __init__(self,length,width):
  #      super().__init__(length,width)

   # def area(self):
    #        return self.length*self.width

#class Cube(Rectangle):
 #   def __init__(self,length,width,height):
  #      super().__init__(length,width)
   #     self.heigth=height

    #def vol(self):
     #   return self.length*self.width*self.heigth

#square=Square(3,3)
#cube=Cube(5,5,5)

#print(square.area())
#print(cube.vol())

#class Rectangle:
    #def __init__(self,length,width):
      #  self.length=length
   #     self.width=width

#class Square(Rectangle):
   # def __init__(self,length,width):
      #  super().__init__(length,width)

   # def area(self):
   #     return self.length*self.width

#class Cube(Rectangle):
    #def __init__(self,length,width,heigth):
        #super().__init__(length,width)
       # self.heigth=heigth

    #def vol(self):
   #     return self.length*self.width*self.heigth

#cube=Cube(6,6,6)
#square=Square(7,7)

#print(square.area())
#print(cube.vol())

