# def number(bus_stops):
#     f_list = []
#     s_list = []
#     for x in bus_stops:
#         f_list.append(x[0])
#         s_list.append(x[1])
#     r = (sum(f_list)-sum(s_list))
#     if r > 0:
#         return r
#     return 0


# def find_it(seq):
#     f_list = []
#     for x in seq:
#         f_list.append(x)
#     for y in f_list:
#         if f_list.count(y) % 2 == 1:
#             return y


# def is_even(n):
#     if n != int:
#         return True if n % 2 == 0 else False


# def remove(s):
#     for i in s:
#         if s[-1] == "!":
#             # removes the last character
#             s = s[:-1]
#     return s


# def decrypt(text, n):
#     f_list = ""
#     s_list = ""
#     if text == "" or int(n) < 0:
#         return text
#     for q in range(0, n):
#         for x in text:
#             if str(text).index(x) % 2 == 1:
#                 f_list += x
#             elif str(text).index(x) % 2 == 0:
#                 s_list += x
#         text = f_list+s_list
#         f_list = ""
#         s_list = ""
#     return text
#
#
# def encrypt(encrypted_text, n):
#     f_list = ""
#     s_list = ""
#     if encrypted_text == "" or int(n) < 0:
#         return encrypted_text
#     for q in range(0, n):
#         for x in encrypted_text:
#             if str(encrypted_text).index(x) % 2 == 0:
#                 f_list += x
#             elif str(encrypted_text).index(x) % 2 == 1:
#                 s_list += x
#         encrypted_text = f_list+s_list
#         f_list = ""
#         s_list = ""
#     return encrypted_text


# print(decrypt("This is a test!", 1))
# print(encrypt("This is a test!", 1))


# def binary_array_to_number(arr):
#     s = int("".join(map(str, arr)), base=2)
#     return s


# def sum_triangular_numbers(n):
#     l = 0
#     s = 0
#     for i in range(n):
#         l += i+1
#         s += l
#     return s


# def points(games):
#     re = 0
#     for x in games:
#         y = x.split(":")
#         print(y)
#         if y[0] > y[1]:
#             re += 3
#         elif y[0] == y[1]:
#             re += 1
#     return re


# def people_with_age_drink(age):
#     return "drink" + ("toddy" if age < 14 else "coke" if age < 18 else "beer" if age < 21 else "whisky")


# def whatday(num):
#     return "Sunday" if num == 1 else "Monday" if num == 2 else "Tuesday" if num == 3 else "Wednesday" if num == 4 else "Thursday" if num == 5 else "Friday" if num == 6 else "Saturday" if num == 7 else "Wrong, please enter a number between 1 and 7"


# def whatday(num):
#     f_list = [[1, "Sunday"], [2, "Monday"], [3, "Tuesday"], [4, "Wednesday"], [5, "Thursday"], [6, "Friday"], [7, "Saturday"]]
#     for x, y in enumerate(f_list):
#         if num-1 == x:
#             return y[1]


# def whatday(num):
#     days = {
#         1: "Sunday",
#         2: "Monday",
#         3: "Tuesday",
#         4: "Wednesday",
#         5: "Thursday",
#         6: "Friday",
#         7: "Saturday"
#     }
#     wr = "Wrong, please enter a number between 1 and 7"
#     return days.get(num, wr)


# def whatday(num):
#     if not num > 7:
#         return ('Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[num-1]
#     return "Wrong, please enter a number between 1 and 7"


# def min_sum(arr):
#     arr = sorted(arr)
#     f_list = []
#     s_list = []
#     re = []
#     print(arr)
#     for x in arr[int(len(arr)/2):]:
#         f_list.append(x)
#     for y in arr[:int(len(arr)/2)]:
#         s_list.append(y)
#     s_list = list(reversed(s_list))
#     for m, n in zip(f_list, s_list):
#         re.append(m*n)
#     return sum(re)


# def persistence(n):
#     n = str(n)
#     count = 0
#     while len(n) > 1:
#         p = 1
#         for i in n:
#             p *= int(i)
#         n = str(p)
#         count += 1
#     return count


# def vert_mirror(s):
#     pass
# def hor_mirror(strng):
#     f_list = []
#     for y in strng.split("\\"):
#         f_list.append(y)
#     return "\\".join(list(reversed(f_list)))
# def oper(fct, s):
#     return hor_mirror(s) if fct == hor_mirror else vert_mirror(s)


# def find_longest(arr):
#     f_list = []
#     for x in arr:
#         f_list.append(len(str(x)))
#     return arr[f_list.index(max(f_list))]


# def find_longest(arr):
#     fva = 0
#     for x in arr:
#         if len(str(x)) > len(str(fva)):
#             fva = x
#     return fva
#
#
# def find_longest_2(arr):
#     sva = 0
#     for y in arr:
#         if len(str(y)) > len(str(sva)):
#             sva = y
#     return sva
#
#
# def find_longest_again(arr):
#     fva = len(str(max(arr)))
#     for q in arr:
#         if len(str(q)) == fva:
#             return q


# def solve(s):
#     inter = []
#     inter2 = ""
#     for a in s:
#         if a in "aeiou":
#             inter.append(inter2)
#             inter2 = ""
#         else:
#             inter2 += a
#     values = []
#     for a in inter:
#         temp = 0
#         for b in a:
#             temp += (ord(b)-96)
#         values.append(temp)
#     return max(values)


# def quote(fighter):
#     return "I am not impressed by your performance." if str(fighter).lower() == "george saint pierre" else "I'd like to take this chance to apologize.. To absolutely NOBODY!" if str(fighter).lower() == "conor mcgregor" else False

# Unsolved
# def capitalize(s):
#     f_list = []
#     s_list = []
#     print(s.lower())
#     for x in s:
#         if s.index(x) % 2 == 1:
#             f_list.append(str(x).upper())
#         else:
#             f_list.append(x)
#     for y in str(s).upper():
#         if s.index(y) % 2 == 0:
#             s_list.append(str(y).upper())
#         else:
#             s_list.append(y)
#     return ["".join(f_list), "".join(s_list)]
# Unsolved


# def pillars(num_pill, dist, width):
#     dist = dist*100
#     re = width * (num_pill - 2) + (num_pill - 1) * dist
#     return re if re > 0 else 0


# def sort_gift_code(code):
#     return sorted(code)


# def longest(a1, a2):
#     re = ""
#     for x in a1:
#         if not x in re:
#             re += x
#     for y in a2:
#         if not y in re:
#             re += y
#     return "".join(sorted(re))


# def nb_year(p0, percent, aug, p):
#     co = 0
#     while p > p0:
#         p0 = p0 + p0 * (percent/100) + aug
#         co += 1
#     return co


# def positive_sum(arr):
#     return sum([x for x in arr if x > 0])


# def find_short(s):
#     return min([len(x) for x in s.split()])


# def find_needle(haystack):
#     for x in haystack:
#         if x == "needle":
#             return f"found the needle at position {str(haystack.index(x))}"


# def digitize(n):
#     f_list = []
#     for x in str(n):
#         f_list.append(int(x))
#     return list(reversed(f_list))


# def disemvowel(string_):
#     return "".join([x for x in string_.lower() if x not in "AEIOUaeiou"])


# def count_by(x, n):
#     f_list = []
#     for q in range(0, n*x+1, x):
#         f_list.append(q)
#     return f_list


# import math
#
# def get_middle(s):
#     re = ""
#     x = math.floor(len(s)/2)
#     if len(s) % 2 == 0:
#         re = re + s[x-1] + s[x]
#     else:
#         re = re + s[x]
#     return re


# def correct(s):
#     return s.replace("5", "S").replace("0", "O").replace("1", "I")


# def get_count(sentence):
#     re = 0
#     for x in sentence:
#         re += 1 if x in "aeiou" else False
#     return re


# Fail
# import string
#
# alphabet = string.ascii_lowercase
# def number(lines):
#     f_list = []
#     for x in lines:
#         try:
#             if x in alphabet:
#                 f_list.append(str(alphabet.index(x) + 1) + ": " + x)
#         except ValueError:
#             pass
#     return f_list


# import string
# alphabet = string.ascii_lowercase
# def words_to_marks(s):
#     f_list = []
#     for x, y in enumerate(alphabet):
#         for q in s:
#             if q in y:
#                 f_list.append(x+1)
#     return sum(f_list)


# def digital_root(n):
#     while n > 9:
#         f_list = []
#         for x in str(n):
#             f_list.append(x)
#             n = sum(f_list)
#     return n


# def high(x):
#     index=" abcdefghijklmnopqrstuvwxyz"
#     x=x.split(" ")
#     bestval=0
#     word=None
#     for i in x:
#         val=0
#         for j in i:
#             val+=index.index(j)
#         if val > bestval:
#             bestval=val
#             word=i
#     return word


# def count(string):
#     f_dict = {}
#     for x in string:
#         if x in f_dict:
#             f_dict[x] += 1
#         else:
#             f_dict[x] = 1
#     return f_dict


# def tribonacci(signature, n):
#     f_list = [x for x in signature]
#     co = 0
#     if n < 3:
#         return signature[:n]
#     while n > co + 3:
#         f_list.append(sum(f_list[-3:]))
#         co += 1
#     return f_list


# def say_hello(name, city, state):
#     return f"Hello, {' '.join(x for x in name)}! Welcome to {city}, {state}"


# def string_expansion(s):
#     fva = ""
#     sva = 1
#     for x in s:
#         if x.isnumeric():
#             sva = int(x)
#         else:
#             fva += x*sva
#     return fva


# def reverse_alternate(s):
#     f_list = []
#     print(s.split())
#     for x in s.split():
#         if s.split().index(x) % 2 == 1:
#             f_list.append(x[::-1])
#         else:
#             f_list.append(x)
#     return " ".join(f_list)


# def is_triangle(a, b, c):
#     x = abs(b - c) < a < b + c
#     y = abs(a - c) < b < a + c
#     z = abs(a - c) < c < a + b
#     if (x, y, z) == (True, True, True):
#         return True
#     return False


# def decrypt(text, n):
#     if text in ("", None):
#         return text
#
#     ndx = len(text) // 2
#
#     for i in range(n):
#         a = text[:ndx]
#         b = text[ndx:]
#         text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
#     return text


# def cube_odd(arr):
#     re = 0
#     for x in arr:
#         if type(x) != int:
#             return None
#         else:
#             if x % 2 == 1:
#                 re += x**3
#     return re


# def maxSequence(arr):
#     max, curr = 0, 0
#     for x in arr:
#         curr += x
#         if curr < 0:
#             curr = 0
#         if curr > max:
#             max = curr
#     return max
#
# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])

# def maxSequence_2(arr):
#     co = 0
#     re = 0
#     for q in arr:
#         co += q
#         if co < 0:
#             co = 0
#         if co > re:
#             re = co
#     return re


# def max_diff(lst):
#     return max(lst) - min(lst) if lst else 0


# def to_float_array(arr):
#     f_list = []
#     for x in arr:
#         if str(x).replace(".", "").replace("-", "").isnumeric():
#             f_list.append(float(x))
#     return f_list


# def mango(quantity, price):
#     return (quantity - quantity // 3) * price


# def remove(s):
#     try:
#         return s[:-1] if s[-1] == "!" else s
#     except IndexError:
#         return ""


# def sum_cubes(n):
#     re = 0
#     for x in range(n + 1):
#         re += x**3
#     return re


# def balanced_num(number):
#     numb = [int(x) for x in str(number)]
#     fva = 0
#     sva = 0
#     while len(number) > 2:
#         fva += numb.pop(0)
#         sva += numb.pop(-1)
#     return "Balanced" if fva == sva else "Not Balanced"
#
#
# def calc(x):
#     fva = ""
#     for y in x:
#         fva += str(ord(y))
#     sva = str(fva).replace("7", "1")
#     return abs(sum(int(q) for q in fva)) - (sum(int(z) for z in sva))
#
#
# def wave(people):
#     f_list = []
#     for x in range(len(people)):
#         if people[x].isalpha():
#             f_list.append(people[:x] + people[x].upper() + people[x + 1:])
#     return f_list


# def max_product(lst, n_largest_elements):
#     co = 1
#     for x in range(n_largest_elements):
#         co *= max(lst)
#         lst.remove(max(lst))
#     return co


# def men_from_boys(arr):
#     f_list = []
#     s_list = []
#     for x in arr:
#         if x % 2 == 0:
#             f_list.append(x)
#         else:
#             s_list.append(x)
#     f_list = sorted(f_list)
#     f_list.extend(sorted(s_list, reverse=True))
#     t_list = []
#     for q in f_list:
#         if q in t_list:
#             pass
#         else:
#             t_list.append(q)
#     return t_list


# def round_to_next5(n):
#     return n - n % 5 + 5 if not n % 5 == 0 else n

#
# import math
# def distance_between_points(a, b):
#     return math.sqrt((abs(a[1] - b[1]) ** 2) + (abs(a[0] - b[0]) ** 2))


# def square_digits(num):
#     fva = ""
#     for x in str(num):
#         if num.counter(x) > 2:
#             fva += str(int(x)**2)
#     return fva


# def find_digit(num, nth):
#     try:
#         num = "".join(list(reversed(str(num))))
#         return num[nth - 1] if nth > 0 else -1
#     except IndexError:
#         return 0


# def up_array(arr):
#     if not arr or min(arr) < 0 or max(arr) > 9:
#         return None
#     for i in range(len(arr) - 1, -1, -1):
#         arr[i] += 1
#         if arr[i] < 10:
#             return arr
#         else:
#             arr[i] = 0
#     return [1] + arr


# def alphabet_war(fight):
#     leftside = 0
#     rightside = 0
#     fva = {"w": 4, "p": 3, "b": 2, "s": 1}
#     sva = {"m": 4, "q": 3, "d": 2, "z": 1}
#     for x in fight:
#         if x in fva.keys():
#             leftside += fva[x]
#         elif x in sva.keys():
#             rightside += sva[x]
#     return "Left side wins!" if leftside > rightside else "Right side wins!" if rightside > leftside else "Let's fight again!"


# def tidyNumber(n):
#     return True if "".join(sorted(str(n))) == str(n) else False


# def find_smallest(numbers, to_return):
#     return numbers.index(min(numbers)) if to_return == "index" else min(numbers) if to_return == "value" else False


# def encode(message, key):
#     abc_dict = {
#         'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
#         'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
#         'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
#         'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
#     }
#     num_list = []
#     key_list = str(key)
#     x = 0
#     for i in message:
#         num_list.append(abc_dict[i] + int(key_list[x]))
#         x += 1
#         if x >= len(key_list):
#             x = 0
#     return num_list


# def vaporcode(s):
#     s = "".join(s.split())
#     re = ""
#     for x in s:
#         re += x.upper() + "  "
#     return re.strip()














