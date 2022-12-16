# def digit(n):
#     return map(int,str(n)[::-1])
# print(list(digit(789)))

# def count_by(x,n):
# return [i*x for i in range(1,n+1)]

# from typing import List
# def process_items(items: List[str]):
#     for item in items:
#         print(item)

# from typing import Optional
# def say_hi(name: Optional[str] = None):
#     if name is not None:
#         print(f"Hey {name}!")
#     else:
#         print("Hello World")

# swapcase

# def str_count(strng, letter):
#     return strng.count(letter)

# def two_sort(array):
#     return "***".join(min(array))

# def divisors(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n / i % 1 == 0:
#             count += 1
#     return count


# def get_count(sentence):
#     counter=0
#     for x in sentence:
#         if x in "aeiouAEIOU":
#             counter+=1
#     return counter


# def hoop_counter(m):
#     return ("Great, now move on to tricks" if m>=10 else "Keep at it until you get it" )


# def greet(name):
#     return f"Hello {name} how are you doing today"

        #-----

# def maps(a):
#     b = list()
#     for i in range(len(a)):
#         b.append(a[i]*2)
#     return b
#
# print(maps(""))

        #-----

# def remove_url_anchor(url):
#     return url.partition("#")[0]
# def remove_url_anchor(url):
#     return url.split("#")[0]

# def between(a, b):
#     list=[]
#     for x in range(a,b+1):
#         list.append(x)
#     return list

# def summation(num):
#     r=0
#     for x in range(1,num+1):
#         r = r+num
#     return r

# def minimum(arr):
#     for x in arr:
#         return  min(arr)

# def count(string):
#     dict={}
#     for x in string:
#         if x in dict:
#             dict[x] += 1
#         else:
#             dict[x] = 1
#     return dict


# def sum_tow_smallest_numbers(numbers):
        # return sorted(numbers)[0]+sorted(numbers)[1]

# def twice_as_old(dad_years_old, son_years_old):
#     x=(dad_years_old)-(son_years_old)
#     y = (x)-(son_years_old)
#     if y < 0:
#         return y*(-1)
#     else:
#         return y


# def abbrev_name(name):
#     q=name.split()[1]
#     y=q[0]
#     for x in name:
#         if x == name[0]:
#             return ( x.upper()+"."+y.upper())
#         else:
#             pass

# import math
# def find_next_square(sq):
        # root = sq ** 0.5
#     x = math.sqrt(sq)
#     if x == int(x):
#         return (x + 1) ** 2
#     else:
#         return (-1)

# from enum import Enum
# class Season(Enum):
#     SPRING = 1
#     SUMMER = 2
#     AUTUMN = 3
#     WINTER = 4


# def array_diff(a,b):
#     if b[0] in a:
#         a.remove(b[0])
#     else:
#         pass
#     return a


# def smash(words):
#     r = ""
#     for x in str(words):
#         r += x.replace(","," ").replace("'","")
#     return "".join(str(q)for q in r)
#
# print(smash(["asdqwe","zxczx","qwedac"]))


# def find_uniq(arr):
#     r=sorted(arr)
#     if r:
#         if r[0] == r[1]:
#             return r[::-1][0]
#         else:
#             return r[0]

# from base64 import b64encode
# from os import urandom
#
# random_bytes = urandom(64)
# token = b64encode(random_bytes).decode()
#
# print(token)


# def goose_filter(birds):
#     my_list = []
#     for x in geese:
#         my_list.append(x)


# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# def goose_filter(birds):
#     list_1 = []
#     for q in birds.split(""):
#         list_1.append(q)
#     for g in geese:
#         if g in list_1:
#             list_1.remove(g)
#             return list_1
#         else:
#             return list_1


# def duplicate_encode(word):
#     res_list = []
#     final_list = []
#     for x in word:
#         res_list.append(x)
#         if res_list.count(x) > 1:
#             final_list.append(")")
#         else:
#             final_list.append("(")
#     return final_list


# def two_sum(numbers, target):
#     list_1 = []
#     list_1 = sorted(list_1)
#     for x in numbers:
#         for y in numbers:
#             if x*y == target:
#                 list_1.append(x)
#                 list_1.append(y)
#                 return list_1
#
#
# print(two_sum([7, 8, 9], 72))











