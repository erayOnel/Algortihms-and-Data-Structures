# class Solution(object):
#     def runningSum(self, nums):
#         fva = 0
#         f_list = []
#         for x in nums:
#             fva += x
#             f_list.append(fva)
#         return f_list


# class Solution(object):
#     def maximumWealth(self, accounts):
#         f_list = []
#         fva = 0
#         print(accounts)
#         for x in accounts:
#             for q in x:
#                 fva += q
#             f_list.append(fva)
#             fva = 0
#         return max(f_list)


# class Solution(object):
#     def fizzBuzz(self, n):
#         f_list = []
#         for x in range(1, n + 1):
#             if x % 15 == 0:
#                 f_list.append("FizzBuzz")
#             elif x % 3 == 0:
#                 f_list.append("Fizz")
#             elif x % 5 == 0:
#                 f_list.append("Buzz")
#             else:
#                 f_list.append(str(x))
#         return f_list


# class Solution(object):
#     def numberOfSteps(self, num):
#         co = 0
#         while num > 0:
#             if num % 2 == 0:
#                 num = num / 2
#                 co += 1
#             else:
#                 num = num - 1
#                 co += 1
#         return co


# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         for c in ransomNote:
#             if c not in magazine:
#                 return False
#             magazine = magazine.replace(c, '', 1)
#         return True


# Timeout
# class Solution(object):
#     def makeIntegerBeautiful(self, n, target):
#         fva = 0
#         first_n = n
#         while True:
#             for q in str(n):
#                 fva += int(q)
#             if fva > target:
#                 n += 1
#                 fva = 0
#             else:
#                 return n - first_n
#
# print(Solution().makeIntegerBeautiful(16, 4))


# def makeIntegerBeautiful(n, target):
#     n0 = n
#     i = 0
#     while sum(map(int, str(n))) > target:
#         n = n // 10 + 1
#         i += 1
#     return n * (10 ** i) - n0


# class Solution:
#     def minimumRecolors(self, blocks: str, k: int) -> int:
#         lis=[]
#         for i in range(0,len(blocks)):
#             count_b=blocks[i:i+k].count("B")
#             if(count_b>=k):
#                 return 0
#             lis.append(k-count_b)
#         return min(lis)


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         l1, l2 = int("".join(str(q) for q in reversed(l1))), int("".join(str(q) for q in reversed(l2)))
#         return list(reversed(list(int(z) for z in str(l1 + l2))))


# def romanToInt(s):
#     roman = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000
#     }
#     res = 0
#     for x in range(len(s)):
#         if x + 1 < len(s) and roman[s[x]] < roman[s[x + 1]]:
#             res -= roman[s[x]]
#         else:
#             res += roman[s[x]]
#     return res


# class Solution(object):
#     def searchInsert(self, nums, target):
#         for x in nums:
#             if x == target:
#                 return nums.index(target)
#         nums.append(target)
#         return sorted(nums).index(target)


# class Solution(object):
#     def lengthOfLastWord(self, s):
#         return len(s.split()[-1])


# class Solution(object):
#     def plusOne(self, digits):
#         return [int(x) for x in str(int("".join(str(q) for q in digits)) + 1)]


# class Solution:
#     def generate(self, numRows):
#         res = [[1]]
#         for x in range(numRows - 1):
#             f_list = [0] + res[-1] + [0]
#             s_list = []
#             for q in range(len(res[-1]) + 1):
#                 s_list.append(f_list[q] + f_list[q + 1])
#             res.append(s_list)
#         return res


# class Solution(object):
#     def containsDuplicate(self, nums):
#         f_set = set()
#         for x in nums:
#             if x in f_set:
#                 return True
#             else:
#                 f_set.add(x)
#         return False


# class Solution(object):
#     def twoSum(self, nums, target):
#         for index, x in enumerate(nums):
#             for index_2, y in enumerate(nums):
#                 if x + y == target and not index == index_2:
#                     return index, index_2


# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         nums1 = sorted(nums1[:m] + nums2[:n])
#         return nums1


# class Solution(object):
#     def sortedSquares(self, nums):
#         return sorted(x**2 for x in nums)


# class Solution(object):
#     def rotate(self, nums, k):
#         q = k % len(nums)
#         try:
#             for x in range(q):
#                 nums.insert(0, nums.pop())
#             return nums
#         except ZeroDivisionError:
#             return nums
# Fail


# class Solution(object):
#     def isIsomorphic(self, s, t):
#         if not len(set(s)) == len(set(t)):
#             return False
#         f_list, s_list = [ord(q) for q in s if s.count(q) > 1], [ord(m) for m in t if t.count(m) > 1]
#         print(f_list, s_list)
#         if not f_list and not s_list:
#             return True
#         print(f_list, s_list)
#         return len(set(f_list)) == 1 and len(set(s_list)) == 1
# Fail


# import math
# class Solution(object):
#     def isSymmetric(self, root):
#         for x in range(int(math.sqrt(len(root))) + 1):
#             s_list = (root[:2**x])
#             root = root[2**x:]
#             print(s_list)
#             # print("toLeft", s_list[(len(s_list) // 2):])
#             # print("toRight", s_list[:(len(s_list) // 2)][::-1])
#             if not s_list == [1]:
#                 if not s_list[(len(s_list) // 2):] == s_list[:(len(s_list) // 2)][::-1]:
#                     return False
#         return True
#         # return s_list[(len(s_list) // 2):] == s_list[:(len(s_list) // 2)][::-1]
# print(Solution().isSymmetric([1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]))
# print(Solution().isSymmetric([1,2,2,3,4,4,3]))
# print(Solution().isSymmetric([1,2,2,None,3,None,3]))


# class Solution(object):
#     def reverseWords(self, s):
#         return " ".join("".join([q for q in reversed(s)]).split()[::-1])


# import math
# class Solution(object):
#     def countOdds(self, low, high):
#         if high - low < 3:
#             if high - low == 0:
#                 return 1 if low % 2 == 1 else 0
#             return 1
#         if low % 2 == 0:
#             return int(math.floor((high - low) // 2)) + 1
#         return ((high - low) // 2) + 1
# print(Solution().countOdds(0,10))
# print(Solution().countOdds(14, 17))
# print(Solution().countOdds(3,3))
# print(Solution().countOdds(11,17))
# print(Solution().countOdds(21,22))
# print(Solution().countOdds(5,9))
# print(Solution().countOdds(4,10))
# print(Solution().countOdds(3,9))
# print(Solution().countOdds(800445804,979430543))
# print(Solution().countOdds(8,10))


# class Solution(object):
#     def subtractProductAndSum(self, n):
#         fva = 1
#         for q in str(n):
#             fva *= int(q)
#         return fva - sum((int(q) for q in str(n)))


# class Solution(object):
#     def moveZeroes(self, nums):
#         # fva = ["".join(str(z) for z in nums if str(z) == "0")]
#         # print(fva)
#         # nums = nums + fva * "0"
#         # print(nums)
#         q = nums.count(0)
#         for x in range(q):
#             nums.remove(0)
#             nums.append(0)
#         return nums


# class Solution(object):
#     def canMakeArihmetic(self, arr):
#         f_list = []
#         for x in range(len(arr) - 1):
#             f_list.append(arr[x] - arr[x + 1])
#         return len(set(f_list)) == 1


# class Solution(object):
#     def areAlmostEqual(self, s1,s2):
#         if s1 == s2:
#             return True
#         if sorted(s1) != sorted(s2):
#             return False
#         f_list = list(zip(s1, s2))
#         s_list = []
#         for x, y in f_list:
#             if not x == y:
#                 s_list.append(x)
#         print(f_list)
#         print(s_list)
#         return len(s_list) == 2


# class Solution(object):
#     def defineSomething(self, arr):
#         fva = 1
#         for x in arr:
#             fva *= x
#         return 1 if fva > 0 else -1 if fva < 0 else 0 if fva == 0 else None


# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         fva = ""
#         s_list = []
#         for x in s:
#             if not x in fva:
#                 fva += x
#             else:
#                 s_list.append(fva)
#                 fva = "" + x
#         s_list.append(fva)
#         try:
#             return len(max(s_list, key=len)), s_list, fva
#         except ValueError:
#             return len(s)
# fail

# print(Solution().lengthOfLongestSubstring("dvdf"))
# print(Solution().lengthOfLongestSubstring("aab"))
# print(Solution().lengthOfLongestSubstring("abcabcbb"))
# print(Solution().lengthOfLongestSubstring("bbbbb"))
# print(Solution().lengthOfLongestSubstring("pwwkew"))
# print(Solution().lengthOfLongestSubstring("abcqqxyzmq"))
# print(Solution().lengthOfLongestSubstring("   "))


# class Solution(object):
#     def firstUniqChar(self, s):
#         for index, q in enumerate(s):
#             if s.count(q) == 1:
#                 return index
#         return -1


# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         for x in ransomNote:
#             if not x in magazine:
#                 return False
#         for q in ransomNote:
#             if magazine.count(q) < ransomNote.count(q):
#                 return False
#         return True


# class Solution(object):
#     def frequencySort(self, s):
#         f_dict = {}
#         s_list = []
#         for x in s:
#             if not x in f_dict:
#                 f_dict[x] = 1
#             else:
#                 f_dict[x] += 1
#         for m, n in list(zip(f_dict.keys(), f_dict.values())):
#             s_list.append(m * n)
#         return "".join(sorted(s_list, key=len, reverse=True))


# class Solution(object):
#     def arraySign(self, nums):
#         fva = 1
#         for x in nums:
#             fva *= x
#         return 1 if fva > 0 else 0 if fva == 0 else -1 if fva < 0 else None


# from functools import reduce
# class Solution(object):
#     def arraySignBetter(self, nums):
#             return reduce(lambda x, y: x * y, nums)


# class Solution(object):
#     def canMakeArithmeticProgression(self, arr):
#         arr = sorted(arr)
#         fva = arr[1] - arr[0]
#         f_list = []
#         try:
#             for x in range(arr[0], arr[-1] + 1, fva):
#                 f_list.append(x)
#         except ValueError:
#             return len(set(arr)) == 1
#         return f_list == arr


# class Solution(object):
#     def findDifference(self, nums1, nums2):
#         return [x for x in set(nums1) if not x in nums2], [y for y in set(nums2) if not y in nums1]


# class Solution(object):
#     def reverseBits(self, n):
#         f_list = []
#         s_list = []
#         n = str(n)[::-1]
#         for x in range(len(n)):
#             f_list.append(2 ** x)
#         for y in n:
#             s_list.append(int(y))
#         t_list = []
#         for m, n in zip(f_list, s_list):
#             t_list.append(m * n)
#         return sum(t_list)


# class Solution(object):
#     def makeGood(self, s):
#         for x in s:
#             if x.isupper():
#                 if s[s.index(x) - 1] == x.islower():
#                     s = s.replace(s[s.index(x) - 1], "", 1)
#                     s = s.replace(x, "", 1)
#         return s


# class Solution(object):
#     def reverse(self, x):
#         if not x or not type(x) == int:
#             return 0
#         output = int("".join([q for q in str(x)[::-1]])) if x > 0 else 0 - int("".join([q for q in str(x)[:0:-1]]))
#         return output if -2**31 < output < 2**31 - 1 else 0


# class Solution(object):
#     def dominantIndex(self, nums):
#         fva = max(nums)
#         nums.remove(fva)
#         for x in nums:
#             if not fva >= x*2:
#                 return -1
#         return nums.index(max(nums))


# class Solution(object):
#     def halvesAreAlike(self, s):
#         return len([q for q in s[:len(s) // 2] if q in "aeiouAEIOU"]) == len([m for m in s[len(s) // 2:] if m in "aeiouAEIOU"])


# class Solution(object):
#     def removeElement(self, nums, val):
#         while val in nums:
#             nums.remove(val)
#         return len(nums)


# import string
# alphabet = string.ascii_lowercase
# class Solution(object):
#     def getLucky(self, s, k):
#         fva = 0
#         for index, q in enumerate(alphabet):
#             for y in s:
#                 if q == y:
#                     fva += index + 1
#         print(fva)
#         if not k == 1:
#             for x in range(k):
#                 fva = sum([int(q) for q in str(fva)])
#             return fva
#         return fva
# fail probably


# class Solution(object):
#     def findMaxConsecutiveOnes(self, nums):
#         co = 0
#         f_list = []
#         for x in nums:
#             if x == 1:
#                 co += 1
#             else:
#                 f_list.append(co)
#                 co = 0
#         f_list.append(co)
#         print(f_list)
#         return max(f_list)


# def reverse_words(text):
#     f_list = []
#     for index, n in enumerate(text):
#         if n == " ":
#             f_list.append(index)
#     print(f_list)
#     s_list = "".join([q[::-1] for q in text.split()])
#     s_list = list(s_list)
#     for m in f_list:
#         s_list.insert(m, " ")
#     return "".join(s_list)


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


def high_and_low(numbers):
    # ...
    return numbers
