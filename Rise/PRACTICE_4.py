# def first_non_consecutive(arr):
#     co = arr[0] - 1
#     for x in arr:
#         co += 1
#         if not x == co:
#             return x
#     return None


# def number(lines):
#     f_list = []
#     co = 1
#     for q in lines:
#         f_list.append(str(co) + ":" + " " + q)
#         co += 1
#     return f_list


# def square_digits(num):
#     return int("".join([str(z) for z in [int(q)**2 for q in str(num)]]))


# def twoSum(self, nums, target):
#     for index, x in enumerate(nums):
#         for index_2, y in enumerate(nums):
#             if x + y == target and not index == index_2:
#                     return index, index_2


# def comp(array1, array2):
#     f_list = []
#     try:
#         for x in array1:
#             if x ** 2 in array2:
#                 f_list.append(x ** 2)
#         print(f_list, array1, array2)
#         return sorted(f_list) == sorted(array2)
#     except TypeError:
#         return False


# def mxdiflg(a1, a2):
#     if not a2 or not a1:
#         return -1
#     fva = abs(len(max(a1, key=len)) - len(min(a2, key=len)))
#     sva = abs(len(min(a1, key=len)) - len(max(a2, key=len)))
#     return max(fva, sva)


# def how_many_light_sabers_do_you_own(name=""):
#     return 18 if name == "Zach" else 0


# def high_and_low(numbers):
#     return " ".join([str(z) for z in (max([int(q) for q in numbers.split()]), min([int(q) for q in numbers.split()]))])


# def remove_every_other(my_list):
#     return [q for index, q in enumerate(my_list) if index % 2 == 0]


# def wave(people):
#     f_list = [q for q in range(len(people))]
#     s_list = []
#     t_list = []
#     fourth_list = []
#     co = 0
#     for k in f_list:
#         t_list.append(people[k].upper())
#     for m in f_list:
#         s_list.append(people[:m] + people[m + 1:])
#     for q in s_list:
#         fourth_list.append(list(q).insert(co, [z for z in t_list]))
#         # q = list(q).insert(2, "H")
#         # print(q)
#         co += 1
#     return f_list, s_list, t_list, fourth_list


# def is_vow(inp):
#     alp = {
#         97: "a",
#         101: "e",
#         105: "i",
#         111: "o",
#         117: "u"
#     }
#     co = -1
#     for q in inp:
#         co += 1
#         if q in alp:
#             inp[co] = alp.get(q)
#     return inp


# def vowel_indices(word):
# return [index + 1 for index, q in enumerate(word) if q in "aeiouyAEIOUY"]


# def ordered_count(inp):
#     f_dict = {}
#     for q in inp:
#         if q in f_dict:
#             f_dict[q] += 1
#         else:
#             f_dict[q] = 1
#     return list(zip(list(f_dict.keys()), list(f_dict.values())))


# def encrypt_this(text):
#     return " ".join([str(ord(q[0])) + q[1::][::-1] for q in text.split()])


# def over_the_road(address, n):
#     return list(zip([q for q in range(address, n * 2) if q % 2 == 1], [m for m in range(address + 1, n * 2 + 1) if m % 2 == 0][::-1]))


# def adjacent_element_product(array):
#     f_list = []
#     for q in range(len(array) - 1):
#         f_list.append(array[q] + array[q + 1])
#     return max(f_list)


# class Solution(object):
#     def mostCommonWord(self, paragraph, banned):
#         print(paragraph.split())
#         for k in " ".join(paragraph).split():
#             if not k.isalpha():
#                 paragraph = paragraph.replace(k, " ")
#         for z in banned:
#             paragraph = paragraph.lower().replace(z, "")
#         return str("".join([q for q in list(max(paragraph.lower().split(), key=len)) if q.isalpha()]))


# def dig_pow(n, p):
#     co = p
#     f_list = []
#     for q in list(str(n)):
#         f_list.append(int(q) ** co)
#         co += 1
#     print(sum(f_list))
#     return sum(f_list) // n if sum(f_list) % p == 0 else -1


# def longest_consec(strarr, k):
#     f_list = []
#     if not strarr or k < 0 or k > len(strarr):
#         return ""
#     for q in range(len(strarr) - (k - 1)):
#         f_list.append("".join(strarr[q:q + k]))
#     return max(f_list, key=len)


# def max_sum(arr,ranges):
#     f_list = []
#     s_list = []
#     for z in ranges:
#         print(z)
#         for q in range(z[0], z[1] + 1):
#             f_list.append(arr[q])
#         s_list.append(f_list)
#         f_list = []
#     return max([sum(q) for q in s_list])


# def capitalize(s):
#     fva = ""
#     sva = ""
#     for index, m in enumerate(s):
#         if index % 2 == 0:
#             fva += m.upper()
#             sva += m
#         else:
#             fva += m
#             sva += m.upper()
#     return fva, sva


# def title_case(title, minor_words=''):
#     title = " ".join([q.lower().capitalize() for q in title.split()])
#     for m in title.split():
#         if m.lower() in [z.lower() for z in minor_words.split()[1:]]:
#             title = title.replace(m, m.lower())
#     return title
# Fail


# class Solution(object):
#     def largestSumAfterKNegations(self, nums, k):
#         for q in range(k):
#             nums[nums.index(min(nums))] *= -1
#         return sum(nums)


# def multiplication_table(size):
#     co = 1
#     f_list = []
#     for q in range(size):
#         f_list.append([q for q in range(co, size * co + 1, co)])
#         co += 1
#     return f_list


# def get_length_of_missing_array(array_of_arrays):
#     try:
#         if not array_of_arrays or array_of_arrays is None:
#             return 0
#         fva = sorted([len(q) for q in array_of_arrays])
#         sva = [q for q in range(min(fva), max(fva))]
#         print(fva, sva)
#         for z in sva:
#             if not z in fva:
#                 return z
#         return 0
#     except TypeError:
#         return 0


# def dont_give_me_five(start,end):
#     return len([q for q in range(start, end + 1) if not "5" in str(q)])







