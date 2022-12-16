# def data_reverse(data):
#     f_list = []
#     s_list = []
#     t_list = []
#     fourth_list = []
#     fifth_list = []
#     for x in data:
#         f_list.append(x)
#         if len(f_list) % 8 == 0:
#             s_list.extend(f_list)
#             s_list.append(",")
#             f_list = []
#     s_list = "".join(str(q) for q in s_list).split(",")[:-1]
#     for m in s_list:
#         t_list.insert(0, m)
#     for g in t_list:
#         for z in g:
#             fourth_list.append(z)
#     fourth_list = ", ".join(fourth_list)
#     for z in fourth_list:
#         if z.isnumeric():
#             fifth_list.append(int(z))
#     return fifth_list


# def kebabize(string):
#     f_list = []
#     try:
#         for x in str(string):
#             if x.isalpha():
#                 if x.isupper():
#                     f_list.append("-" + x.lower())
#                 else:
#                     f_list.append(x)
#             else:
#                 pass
#         return "".join(f_list) if not f_list[0][0] == "-" else f_list[0][1] + "".join(f_list[1:])
#     except IndexError:
#         return ""


# def sort_my_string(s):
#     fva = ""
#     sva = ""
#     for index, value in enumerate(s):
#         if index % 2 == 0:
#             fva += value
#         else:
#             sva += value
#     return fva + " " + sva


# def max_tri_sum(numbers):
#     return sum(sorted(set(numbers), reverse=True)[0:3])


# def flatten_and_sort(array):
#     f_list = []
#     for x in array:
#         for y in x:
#             if str(y).isnumeric() or type(y) == int:
#                 f_list.append(y)
#     return sorted([int(q) for q in f_list])


# def explode(s):
#     return "".join(int(x) * str(x) for x in s)


# def longest_palindrome(s):
#     m = 0
#     n = len(s)
#     for i in range(n):
#         for j in range(i, n):
#             t = s[i:j + 1]
#             if t == t[::-1]:
#                 m = max(m, len(t))
#     return m


# def multiples(m, n):
# return [x * n for x in range(1, m + 1)]


# def disarium_number(number):
#     f_list = []
#     s_list = []
#     t_list = []
#     for q in range(1, len(str(number)) + 1):
#         f_list.append(q)
#     for x in str(number):
#         s_list.append(x)
#     for m, n in list(zip(s_list, f_list)):
#         t_list.append(int(m) ** int(n))
#     return "Disarium !!" if sum(t_list) == int(number) else "Not !!"


# def array_leaders(numbers):
#     res = []
#     s = 0
#     for n in reversed(numbers):
#         if n > s:
#             res.append(n)
#         s += n
#     res.reverse()
#     return res


# def max_gap(numbers):
#     numbers.sort()
#     last = numbers[0]
#     biggest_diff = 0
#     for num in numbers:
#         diff = num - last
#         if diff > biggest_diff:
#             biggest_diff = diff
#         last = num
#         return biggest_diff


# def capitalize(s, ind):
#     fva = ""
#     for i, n in enumerate(s):
#         if i in ind:
#             fva += str(n).upper()
#         else:
#             fva += n
#     return fva


# def digital_root(n):
#     fva = 0
#     while len(str(n)) > 1:
#         for x in str(n):
#             fva += int(x)
#         n = fva
#         fva = 0
#     return n


# def create_phone_number(n):
# n = "".join(str(q) for q in n)
# return f"({n[:3]}) {n[3:6]}-{n[6:]}"


# def is_valid_walk(walk):
#     for q in walk:
#         if q not in "nswe":
#             return False
#     if not len(walk) == 10:
#         return False
#     else:
#         for z in walk:
#             if walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w"):
#                 return True
#             else:
#                 return False
#     return len(walk) == 10 and walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w")


# def narcissistic( value ):
#     f_list = []
#     for x in str(value):
#         f_list.append(int(x) ** len(str(value)))
#     return True if sum(f_list) == int(value) else False


# def valid_braces(seq):
#     while True:
#         if '()' in seq:
#             seq = seq.replace('()', '')
#         elif '{}' in seq:
#             seq = seq.replace('{}', '')
#         elif '[]' in seq:
#             seq = seq.replace('[]', '')
#         else:
#             return not seq


# def product_array(numbers):
#     result = []
#     for i in range(len(numbers)):
#         count = 1
#         nums = numbers.copy()
#         nums.pop(i)
#         for j in nums:
#             count *= j
#         result.append(count)
#     return result


# def strong_num(number):
#     fva = 1
#     f_list = []
#     num_list = list(str(number))
#     for q in num_list:
#         for x in range(1, int(q) + 1):
#             fva *= x
#         f_list.append(fva)
#         fva = 1
#     return "STRONG!!!!" if sum(f_list) == number else "Not Strong !!"


# def parts_sums(ls):
#     s_list = []
#     for x in range(len(ls) + 1):
#         s_list.append(sum(q for q in ls[x:]))
#     return s_list


# opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
#
#
# def dirReduc(plan):
#     new_plan = []
#     for d in plan:
#         if new_plan and new_plan[-1] == opposite[d]:
#             new_plan.pop()
#         else:
#             new_plan.append(d)
#     return new_plan


# opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
#
#
# def dirReduc(arr):
#     i = 0
#     while i < len(arr) - 1:
#         current = arr[i]
#         next = arr[i + 1]
#         if next == opposite[current]:
#             arr.pop(i)
#             arr.pop(i)
#             i = 0
#         else:
#             i += 1
#     return arr


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


# def order(sentence):
#     data = sentence.split()
#     result = []
#     for word in data:
#         for letter in word:
#             if letter.isdigit():
#                 result.append([int(letter), word])
#     return " ".join([x[1] for x in sorted(result)])


# def accum(s):
#     f_list = []
#     for index, y in enumerate(s.lower()):
#         f_list.append(y.upper() + y * index)
#         f_list.append("-")
#     return "".join(f_list)[:-1]


# import math
# def cockroach_speed(s):
#     return math.floor(s*27.777778)


# def DNA_strand(dna):
#     return dna.translate(str.maketrans("ATGC", "TACG"))


# def capitals(word):
#     f_list = []
#     for index, q in enumerate(word):
#         if q.isupper():
#             f_list.append(index)
#     return f_list


# def order(sentence):
#     f_list = []
#     s_list = []
#     for x in sentence.split():
#         for y in x:
#             if y.isnumeric():
#                 f_list.append(x)
#                 s_list.append(y)
#     t_list = []
#     for q, j in sorted(list(zip(f_list, s_list)), key=lambda x: x[1]):
#         t_list.append(q)
#     return " ".join(t_list)


# def find_even_index(arr):
#     for index, q in enumerate(arr):
#         if sum(arr[:index]) == sum(arr[index + 1:]):
#             return index
#     return -1


# def sort_array(source_array):
#     odd = []
#     for i in source_array:
#         if i % 2 == 1:
#             odd.append(i)
#     odd.sort()
#     x = 0
#     for j in range(len(source_array)):
#         if source_array[j] % 2 == 1:
#             source_array[j] = odd[x]
#             x += 1
#     return source_array


# def reverse_letter(string):
#     return "".join([q for q in string if q.isaplha()])[::-1]


# def expanded_form(num):
#     f_list = []
#     s_list = []
#     for index, q in enumerate(str(num)[::-1]):
#         f_list.append(str(int(q) * (10 ** index)))
#     for m in f_list:
#         if m == "0":
#             pass
#         else:
#             s_list.append(m)
#     return " + ".join(s_list[::-1])


# def multi_table(number):
#     fva = ""
#     for x in range(1, 11):
#         fva += f"{x} * {number} = {x * number}\n"
#     return fva[:-1]


# def warn_the_sheep(queue):
#     if queue[-1] == "wolf":
#         return "Pls go away and stop eating my sheep"
#     for index, q in enumerate(queue[::-1]):
#         if q == "wolf":
#             return f"Oi! Sheep number {index}! You are about to be eaten by a wolf!"


# db_good = {
#     "Hobbits": 1,
#     "Men": 2,
#     "Elves": 3,
#     "Dwarves": 3,
#     "Eagles": 4,
#     "Wizards": 10,
# }
# db_evil = {
#     "Orcs": 1,
#     "Men": 2,
#     "Wargs": 2,
#     "Goblins": 2,
#     "Uruk Hai": 3,
#     "Trolls": 5,
#     "Wizards": 10,
# }
# def good_vs_evil(good, evil):
#     f_list = []
#     s_list = []
#     good, evil = list(good.split()), list(evil.split())
#     # print(list(zip(good, db_good.values())))
#     for x, y in list(zip(good, db_good.values())):
#         f_list.append(int(x) * y)
#     for m, n in list(zip(evil, db_evil.values())):
#         s_list.append(int(m) * n)
#     return "Battle Result: Evil eradicates all trace of Good" if sum(f_list) < sum(s_list) else "Battle Result: Good triumphs over Evil" if sum(f_list) > sum(s_list) else "Battle Result: No victor on this battle field"


# def validate(n):
#     f_list = []
#     if len(str(n)) % 2 == 0:
#         for index, q in enumerate(str(n)):
#             if index % 2 == 0:
#                 f_list.append(int(q) * 2)
#             else:
#                 f_list.append(q)
#     else:
#         for m, n in enumerate(str(n)):
#             if m % 2 == 0:
#                 f_list.append(n)
#             else:
#                 f_list.append(int(n) * 2)
#     print(f_list)
#     for k in f_list:
#         if len(str(k)) > 1:
#             f_list.insert(f_list.index(k), sum([int(m) for m in str(k)]))
#             f_list.remove(k)
#         else:
#             pass
#     return True if sum(int(b) for b in f_list) % 10 == 0 else False


# def unique_in_order(iterable):
#     f_list = []
#     fva = ""
#     for x in iterable:
#         if not x == fva:
#             f_list.append(x)
#             fva = x
#     return f_list


# def is_valid_IP(string):
#     co = 0
#     string = [x for x in string.split(".")]
#     for z in string:
#         if not z.isnumeric():
#             return False
#     try:
#         for q in string:
#             if q[0] == "0" and len(q) > 1:
#                 return False
#             if -1 < int(q) < 256 and len(string) == 4:
#                 co += 1
#         return True if co == 4 else False
#     except IndexError:
#         return False


# def solution(s):
#     f_list = []
#     if len(s) % 2 == 1:
#         s += "_"
#     print(s)
#     for index, q in enumerate(s):
#         if index % 2 == 0:
#             f_list.append(q + s[index + 1])
#     return f_list


# import string
# alp = string.ascii_letters
# def find_missing_letter(chars):
#     chars = str("".join(chars))
#     f_list = []
#     for x in range(alp.index(chars[0]), alp.index(chars[-1]) + 1):
#         f_list.append(alp[x])
#     chars = list(chars)
#     s_list = list(zip(f_list, chars))
#     for m, n in [q for q in s_list]:
#         if not m == n:
#             return m

# def sort_array(source_array):
#     f_list = []
#     s_list = []
#     real_source = []
#     try:
#         for index, q in enumerate(source_array):
#             if q % 2 == 0:
#                 s_list.append(q)
#                 f_list.append(index)
#             else:
#                 real_source.append(q)
#         source_array = sorted(source_array)
#         real_source = sorted(real_source)
#         for x in range(len(f_list)):
#             real_source.insert(f_list[x], s_list[x])
#         return real_source
#     except IndexError:
#         return sorted(source_array)


# def one_two_three(n):
#     ones = (n * "1")
#     modul = str(len(ones) % 9)
#     if n == 0:
#         return [0, 0]
#     return [int((len(ones) // 9 * "9") + str(int(modul) if int(modul) != 0 else "")), int(ones)]


# def generate_hashtag(s):
#     return "#" + "".join(q.capitalize() for q in s.split()) if s and len(s) < 140 else False


# def valid_parentheses(string):
#     fva = ""
#     for x in string:
#         if x == "(" or x == ")":
#             fva += x
#     string = fva
#     while "()" in string:
#         if "()" in string:
#             string = string.replace("()", "")
#     return string == ""


# def scramble(s1, s2):
#     f_dict = {}
#     s_dict = {}
#     f_list = []
#     s_list = []
#     for x in sorted(s1):
#         if x in f_dict:
#             f_dict[x] += 1
#         else:
#             f_dict[x] = 1
#     for y in sorted(s2):
#         if y in s_dict:
#             s_dict[y] += 1
#         else:
#             s_dict[y] = 1
#     print(f_dict)
#     print(s_dict)
#     for q in f_dict.keys():
#         if q not in s_dict.keys():
#             f_dict[q] = 0
#     for g in f_dict.copy():
#         if f_dict[g] == 0:
#             del f_dict[g]
#     print(s_dict)
#     for j in s_dict.copy():
#         if j not in f_dict:
#             del s_dict[j]
#     print(f_dict)
#     print(s_dict)
#     for m in f_dict.values():
#         f_list.append(m)
#     for n in s_dict.values():
#         s_list.append(n)
#     print(list(zip(f_list, s_list)))
#     for w, e in list(zip(f_list, s_list)):
#         if e <= w:
#             return True
#         else:
#             return False


# def to_underscore(string):
#     fva = ""
#     if str(string).isnumeric():
#         return str(string)
#     for x in string:
#         if str(x).isupper():
#             fva += "_" + x.lower()
#         else:
#             fva += x
#     return fva if not fva[0] == "_" else fva[1:]











