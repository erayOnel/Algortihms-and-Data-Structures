#class Book:
    #Types=("Hardcover","Paperback")
   # def __init__(self,name,book_style,writer):
        #self.name=name
        #self.book_style=book_style
      #  self.writer=writer
    #def __str__(self):
       # return f"{self.name} is written by {self.writer} and the style is {self.book_style}"
    #@classmethod
   # def hardcover(cls,name,writer):
   #     return Book(name,Book.Types[0],writer)

#print(Book("Parry Hotter","Hardcover","J.K.Rowling"))
#x=Book("Parry Hotter","Hardcover","J.K.Rowling")
#print(x.name)

#x=Book.hardcover("Parry Hotter","J.K.Rowling")
#print(x)


#class Device:
    #def __init__(self,name,connected_by):
        #self.name=name
        #self.connected_by=connected_by
        #self.connected=True

    #def __str__(self):
      #  return f"Device {self.name!r} ({self.connected_by})"

   # def disconnected(self):
   #     self.disconnected=False
#        print("Disconnected")

#Printer=Device("Printer","USB")
#print(Printer)
#Printer.disconnected()

#class Printer(Device):
    #def __init__(self,name,connected_by,capacity):
        #super().__init__(name,connected_by)
        #self.capacity=capacity
      #  self.remaining_pages=capacity

   # def __str__(self):
      #  return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

   # def will_write(self,page_number):
        #if not self.connected:
         #   print("Printer isn't connected")
            #return
      #  print(f"Printing ({page_number}) pages")
   #     self.remaining_pages -=page_number

#Printer=Printer("Printer","USB",400)
#Printer.will_write(50)
#print(Printer)


#class Bookshelf:
   # def __init__(self,quantity):
      #  self.quantity=quantity

    #def __str__(self):
       # return f"Bookshel has {self.quantity} books"

#shelf=Bookshelf(500)

#class Book(Bookshelf):
   # def __init__(self,name,quantity):
      #  super().__init__(quantity)
       # self.name=name

    #def __str__(self):
       # return f"Book name is {self.name}"

#book=Book("Parry Hotter",500)
#print(book)


#class Bookshelf:
    #def __init__(self,quantity):
       # self.quantity=quantity

    #def __str__(self):
   #     return f"Bookshel has {self.quantity} books"

#shelf=Bookshelf(500)

#class Book(Bookshelf):
   # def __init__(self,name,quantity):
       # super().__init__(quantity)
       # self.name=name

    #def __str__(self):
   #     return f"Book name is {self.name}"

#book=Book("Parry Hotter",500)
#print(book)


#class Bookshelf:
    #def __init__(self,*books):
       # self.books=books

    #def __str__(self):
   #     return f"Bookshel has {len(self.books)} books"

#class Book:
   # def __init__(self,name):
      #  self.name=name

   # def __str__(self):
   #     return f"Book name is {self.name}"

#book1=Book("Parry Hotter")
#book2=Book(":(")
#shelf=Bookshelf(book,book2)
#print(shelf)


#def divide(x,y):
   # if y==0:
      #  raise ZeroDivisionError("Cant' divide to zero")
    #return (x / y)

#notes=[45,85,97,23]
#try:
   # average=divide(sum(notes),len(notes))
    #print(f"Average is {average}")
#except:
   # print("There are no grades in ur list")

#def f1(x):
   # return x**2
#def f2(y,z):
   # return z(y)+8
#print(f1(5))
#print(f2(5,f1))

#x={"a":1,"b":2}
#y={"c":3,"d":4}
#z={**x,**y}
#print(z)


#def my_func(param):
   # def z():
      #  print("First")
        #param()
       # print("Last")
   # return z
#def x():
   # print("Whee!!")
#m=my_func(x)
#m()


#users={"username":"V","access_level":"guest"}

#def admin_getpassw():
   # return "passw is Cane"

#def secure(func):
    #if users["access_level"] == "admin":
       # return func
    #else:
   #     print("You r not an admin")

#admin_getpassw=secure(admin_getpassw())


#user={"username":"Rob","access_level":"admin"}

#def give_passw():
   # return 789

#def security(x):
   # def function_for_secure():
      #  if user["access_level"]=="admin":
           # return x
        #else:
      #      return f"No admin permissions for  {user['username']}"
   # return function_for_secure

#z=security(give_passw())
#print(z())

#from typing import List,Optional

#class Student:
    #def __init__(self,name:str,grades:Optional[List[int]]=None):
        #self.name=name
       # self.grades=grades or []

    #def take_notes(self,notes:int):
   #     self.grades.append(notes)

#Bob=Student("Bob",[45,85,12,35])
#Rolf=Student("Rolf",[26,52,94,32])
#Bob=Student("Bob")
#Rolf=Student("Rolf")
#Bob.take_notes(78)
#Rolf.take_notes(37)
#print(Bob.grades)
#print(Rolf.grades)





















































