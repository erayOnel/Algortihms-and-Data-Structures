#things_in_dunno={"a":35,"b":40,"c":50,"d":60,"e":70}

#things_in_dunno2={key: round((value-32)*(5/9)) for (key,value) in things_in_dunno()}

#'dict comprehension' değerleri için (key,value) değerleri belirtilmeli#

#print(things_in_dunno2)

#weather={'Newyork':'snow','Boston':'sunny','Losangeles':'sunny','Chicago':'cloudy'}
#sunny_weathers={key:value for (key,value) in weather.items() if value=='sunny'}
#print(sunny_weathers)



#cities={'Newyork':35,'Boston':15,'Losangeles':56,'Chicago':29}
#warm_ones={key:('WARM' if value >= 35 else 'COLD') for (key,value) in cities.items()}
#print(warm_ones)

#def check_temps(value):
 #   if value >= 40:
#        return "you r on FIRE"
    #elif value < 30:
   #     return "it's ok"
  #  else:
 #       print("COLD")

#cities={"NewYork":22,"Boston":74,"LosAngeles":12,"Chicago":68}
#fcities={key: check_temps(value) for (key,value) in cities.items()}
#print(fcities)

#print(time.time())
#'epoch' zamanından itibaren ne kadar süre geçtiğini belirtir#
#print(time.gmtime(0))
#time.gmtime(0).tm_mon
#time.gmtime(0).tm_mday
#print(time.ctime())#

#print(time.localtime())
#x=time.localtime()
#print(x.tm_mday,"month is :",x.tm_mon)

#forreadable=time.strftime("%A %B %Y",time.localtime())
#print(forreadable)

#createadate= "11 July Monday 2022"
#print(time.strptime(createadate,"%d %B %A %Y"))
#'strptime' yapısında modüllerin girilen tarihle uyuşduğuna dikkat et#

#'asctime' yapısı:(year,month,day,hours,minutes,seconds,day of the week,day of the year,day savings time)
#time_tuple=(2022,7,11,14,22,0,0,0,0)
#time_string=time.asctime(time_tuple)
#print(time_string)


#import time
#mport threading

#def summon(a,b):
 #   print("Strt")
  #  time.sleep(2)
   # print(a*b)

#def text():
 #   print("End")

#thread_1=threading.Thread(target=summon,args=(5,9))
#thread_2=threading.Thread(target=text)

#thread_1.start()
#thread_2.start()

#thread_1.join()
#thread_2.join()

#print("sıjfndkglş")
#join fonksiyonları belirtilen thread'lerı durdurmak için kullanılır

#import time
#from multiprocessing import Process

#def subf1():
 #   print("subf1 başladı")
  #  time.sleep(1.5)
   # print("subf1 sonlandı")

#def subf2():
 #   print("subf2 başladı")
  #  time.sleep(1.5)
   # print("subf2 sonlandı")

#def mainfunc():
 #   print("mainf başladı")
  #  process_1=Process(target=subf1)
   # process_2=Process(target=subf2)
    #process_1.start()
#    process_2.start()
 #   process_1.join()
  #  process_2.join()
   # print("mainf sonlandı")

#if __name__ == "__main__":
 #   mainfunc()


#num1=2
#num2=8
#print(num1 *num2)

#def for_multi(num1,num2):
 #   print(num1*num2)
#for_multi(4,4)

#def for_multiply(num1,num2):
 #   return(num1*num2)
#print(for_multiply(1,16))

#forf="asd"
#print(f"birgarip{forf}")
#'fstring'

#name="BOB"
#secondone=f"Welcome {name}"
#print(secondone.format(name))

#knowable="things {} things {}"
#hmm=knowable.format("lol","olo")
#print(hmm)

#givetheage=int(input("Give a age: "))
#formonth=givetheage*12
#z=int(formonth)
#print(z,"is your age by month")

#p="practice"
#n="f"
#print(f"some {p} for {n} string")


#a={"asd","zxc","g","h","j"}
#b={"b","c","d","asd","zxc"}

#print(a.intersection(b))
#print(a.union(b))
#print(a.difference(b))


#set1={14,5,9,31,12,77,67,8}
#set2={5}
#set2.add(9)
#set2.add(12)
#set2.add(77)
#set2={5,9,12,77}
#print(set1)
#print(set2)
#print(set1.intersection(set2))

#import random

#while True:
    #x=random.randint(1,11)
    #user_guess=input("Write 'y' if you wanna guess something: ")

    #if user_guess=="y":
       # user_number=int(input("Guess our digit number: "))

    #if user_number == x:
       # print("Right")
    #else:
      #  print("Next time")
   # print("The number is : ",x)

    #z=(input("Do yu wan' play again ('y') : "))
   # if z != "y":
        #print("Thanks for playing")
        #break

#movies=("Whiplash","Matrix","Shawshank")
#z=("Matrix")
#print(z in movies)

#notes=[95,20,56,74,35,18]
#amount=0
#for z in notes:
   # amount += z
#x=(len(notes))
#print(amount//x)


#nums=[5,9,4,2,8]
#double=[]
#for x in nums:
   # double.append(x*2)
#print(double)

#nums_2=[8,1,3,4,6,5,2,7]
#double_2=[z*2 for z in nums_2]
#print(double_2)


#friends=["Sam","Vlad","Samantha","Arthur","Sans","Violet"]
#start_s=[]

#for z in friends:
    #if z.startswith("S"):
   #     start_s.append(z)

#print(start_s)

#friends=["Sam","Vlad","Samantha","Arthur","Sans","Violet"]
#start_s=[z for z in friends if z.startswith("S")]
#print(start_s)

#a="b"
#print(a)
#print(id(a),id("b"))


#friends=[
    #{"name :":"A","age":25},
    #{"name :":"B","age":62},
   # {"name :":"C","age":34},
#]
#for z in friends:
    #print(z)

#print(friends[1])

#students={"Rolf :":65,"Adrian :":23,"Bob :":42}
#for k in students:
#    print(f"{k} :{students[k]}")
#for key,value in students.items():
#    print(f"{key} {value}" )


#ages={"Arthur ":28,"Dimitri ":64,"Javier ":31,"Jim ":25}
#for names,nums in ages.items() :
   # print(f"Name {names},age :{nums}")

#a=("asd",45,"mec")
#x,y,z=a
#print(x)
#d,_,c=a
#print(d,_,c)


#x,*y=[1,6,8,4,5,9,7]
#print(x)
#print(y)

#def hello():
   # print("Hello")
#hello()

#friends=["F1","F2"]
#def addf():
    #x=(input("Give a name "))
   # friends.append(x)
#addf()
#print(friends)


#def sum(x,y):
    #res = x+y
   # print(res)
#sum(5,9)

#def hello(name,surn):
   # print(f"Hello {name} {surn}")
#hello("AB","DC")


#def division(x,y):
    #if y==0:
       # print("Can't divide to zero")
    #else:
   #     print(x/y)
#division(8,0)
#division(5,4)

#def sum(x,y):
    #return
    #return x+y
#print(sum(9,8))


#def division(x,y):
    #if y != 0:
       # print(x/y)
    #else:
   #     print("zero")
#division(8,0)


#def return_42():
    #return 42


#flambda=lambda x,y: x+y
#print(flambda(6,4))
#print((lambda x,y: x+y)(7,8))


#def double(x):
    #return x*2

#list=[7,56,2,18,9,5]

#doubledone=[(lambda x:x*2)(x) for x in list]
#print(doubledone)

#------

#y = [1, 2, 3, 4, 5]
#y_karesi = []
#for i in y:
   # y_karesi.append(i ** 2)

#print(y)
#print(y_karesi)
#map(fonksiyonun ismi,liste)#

#y = [1, 2, 3, 4, 5]
#y_karesi = list(map(lambda x: x**2, y))

#print(y)
#print(y_karesi)


#list_of_tuples = [(1,'apple'), (2,'ball')]
#my_dict = dict(list_of_tuples)
#print(my_dict)
#print(list_of_tuples)
#print(my_dict[1])


#users=[
    #(0,"Bob","passw1"),
    #(1,"Adrian","passw2"),
    #(2,"Nick","passw3"),
   # (3,"Said","passw4"),
#]

#username_mapping={x[1]: x for x in users}


#username_input=input("Give a usern :")
#passw_input=input("Give a passw :")

#_,username,passw=username_mapping[username_input]

#if passw_input == passw:
   # print("Correct password")
#else:
   # print("Wrong password")


#itsdata={"Num1":15,"Num2":68,"Num3":34,"Num4":60}

#def average(itsdata):
   # z=itsdata.values()
#    print(sum(z)/len(z))


#def multiply(*args):
    #total=1
   # for arg in args:
      #  total *= arg
   # return total
#'total ' değerine yeni değer atadığımız için 'return' komutunu kullandık

#print(multiply(8,5,1,6))


#def add(x,y):
   # return x-y
#print(add(y=5,x=9))


#def add(r,q):
   # return r*q
#numbers={"q":5,"r":9}
#print(add(numbers["q"],numbers["r"]))


#def multiply(*args):
    #multiplied = 1
   # for x in args:
      #  multiplied *= x
   # return multiplied
#print(multiply(4,6,51,8,4,65,1))

#def apply(*args,operator):
   # if operator== "*":
      #  return multiply(*args)
    #elif operator=="+":
       # return sum(args)
    #else:
       # return "No valid operator provided to apply"

#print(apply(5,8,4,7,9,operator="*"))


#def remember(**kwargs):
   # print(kwargs)
#remember(A=852,B=1247,C=3549)

#def named(**kwargs):
    #print(kwargs.values())
   # return kwargs.values()
#details={"name" : "Bob" , "age" :25}

#print("Person:",named(**details))


#def k_args(*args,**kwargs):
    #print(args)
   # print(kwargs)

#k_args(8,9,5,1,3,qwe=654)


#student={"name: ":"Rolf","grades":(75,89,45,12,85)}

#def average(x):
   # return sum(x)/len(x)

#print(average(student["grades"]))


#class Student:
   # def __init__(self):
      #  self.name="Vi"
        #self.age=45
        #self.area="Math"

#student=Student()
#print(student.age)


#class Student:
    #def __init__(self,name,grades,areas):
        #self.name=name
        #self.grades=grades
        #self.areas=areas
       # self.grades=grades

    #def average(self):
   #     return round(sum(self.grades)/len(self.grades))

#student=Student("Bob",(48,32,56,74,12,68),"Math")
#anotherone=Student("Arnold",(24,53,15,96,24,70),"Physics")
#print(student.name,end=" ")
#print(student.average(),end=",")
#print("Lesson: ",student.areas,"\n")
#kaçış fonksyionları için '\' kullanmayı unutma
#print(anotherone.name,anotherone.average(),"Lesson: ",anotherone.areas)


#class dunno:
    #def __init__(self,name,age,country):
        #self.name=name
        #self.age=age
      # self.country=country

    #def __str__(self):
   #     return f"{self.name} is {self.age} y/o and livin'n {self.country}"

#print(dunno("Benedick",32,"Canada"))


#class Store:
    #def __init__(self,name):
        #self.name=name
       # self.items=[]

    #def add_item(self,name,price):
       #item={'name':name,'price',price}
     #   self.items.append(item)

  #  def stock_price(self):
#        return sum([item['price'] for item in self.items])


#class Classtest:
   # def instance_method(self):
       # print(f"{self} is the position of method")

    #@classmethod
   # def class_method(cls):
       # print(f"Called class_method of {cls}")

    #@staticmethod
   # def static_method():
   #     print("Called static_method...")

#Classtest.static_method()
#Classtest().class_method()
#Classtest.class_method()














































