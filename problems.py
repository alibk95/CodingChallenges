class Solution:
    # 1
    def moveZeros(self, nums):
        # input : [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
        # output: [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
        t = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[t] = nums[i]
                if i != 0:
                    nums[i] = 0
                t += 1
        return nums

    # 2
    def kth_largest_num(self, nums, k):
        # works with the lists that not have duplications.
        # input: [1,2,3,4,5,6,0,8,9]
        # output: 6
        l = [0 for i in range(k)]
        for j in range(k):
            max = 0
            for i in range(len(nums)):
                if nums[i] > max:
                    max = nums[i]
                    u = i
            l[j] = nums[u]
            nums[u] = 0

        return max, l

    # 3
    def find_single(self, nums):
        # XOR helps to do it very efficient with the space requirement of O(1) and time complexity of O(n)
        # XOR of a number with itself is 0
        # XOR of a number with 0 is the number itself
        res = nums[0]
        # Do XOR of all elements
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res

    # 4
    def two_sum(self, nums, k):
        # [4,7,1,-3,2]
        for i in range(len(nums)):
            nums[i] = nums[i] - k
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == 0:
                    return True
        return False

    # 4
    def two_sum_2(self, nums, k):
        # More pythonic way of doing it
        for i in range(0, len(nums)):
            if k - nums[i] in nums:
                return True
        return False

    # 5
    def longest_length_substring(self, str):
        longest = 0
        aux = []
        for s in str:
            if s in aux:
                aux = aux[aux.index(s) + 1:]
            aux.append(s)
            longest = max(longest, len(aux))
        return longest

    # 7
    def balanced_parenthesis(self, str):
        # [()]{}
        # True
        if str == None:
            return True
        stack = ['#']
        top = stack[-1]
        map = {")": "(", "}": "{", "]": "["}
        for s in str:
            print(s)
            if s in map:
                if stack[-1] == '#':
                    return False
                if stack[-1] != '#':
                    top = stack.pop()
                    print("pop ", stack)
                if map[s] != top:
                    return False
            else:
                stack.append(s)
                print("push ", stack)
        if stack[-1] == '#':
            return True
        else:
            return False

    # 8
    def buy_and_sell(self, nums):
        max = nums[1] - nums[0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] > max:
                    max = nums[j] - nums[i]
        return max

    # 9
    def max_subarray_sum(self, nums):
        # time complexity of O(n)
        max = 0
        t = 0
        for i in range(len(nums)):
            max = max + nums[i]
            if max < 0:
                max = 0
            elif t < max:
                t = max
        return t

    # 11
    def courses_to_take(self, courses):
        # Needs work and improvement
        # input is a hashmap or hash table and to access the hash map we have the following ways:
        # my_dict={'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
        # print(my_dict.keys())
        # print(my_dict.values())
        # print(my_dict.get('Dave'))
        print(courses)
        arr = []
        while len(arr) != len(courses):
            for course in courses:
                if courses.get(course) == arr:
                    arr.append(course)
                    print(arr)

    # 12
    def edit_distance(self, str1, str2, m, n):
        # A Naive recursive Python program to fin minimum number
        # operations to convert str1 to str2
        # If first string is empty, the only option is to
        # insert all characters of second string into first
        if m == 0:
            return n
        # If second string is empty, the only option is to
        # remove all characters of first string
        if n == 0:
            return m
        # If last characters of two strings are same, nothing
        # much to do. Ignore last characters and get count for
        # remaining strings.
        if str1[m-1] == str2[n-1]:
            return self.edit_distance(str1, str2, m-1, n-1)
        # If last characters are not same, consider all three
        # operations on last character of first string, recursively
        # compute minimum cost for all three operations and take
        # minimum of three values.
        return 1 + min(
            self.edit_distance(str1, str2, m, n-1),
            self.edit_distance(str1, str2, m-1, n),
            self.edit_distance(str1, str2, m-1, n-1)
            )

    # 13
    def max_product(self, nums, k):
        res = 1
        arr = []
        maximum = 0
        print(nums)
        for i,num in enumerate(nums):
            for j in range(i+1 ,len(nums)):
                for k in range(j+1, len(nums)):
                    res = nums[i] * nums[j] * nums[k]
                    if res > maximum:
                        maximum = res
        return maximum

    # 13
    def max_product_improved(self, nums, k):
        print(nums)
        max1 = -1000
        max2 = -1000
        max3 = -1000
        min1 = 1000
        min2 = 1000
        for i in range(len(nums)):
            # finding the 3 largest elemets
            if nums[i] > max1:
                max3 = max2
                max2 = max1
                max1 = nums[i]
            elif nums[i] > max2:
                max3 = max2
                max2 = nums[i]
            elif nums[i] > max3:
                max3 = nums[i]
            # finding the 2 lowest elements
            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]
        return max(min1 * min2 * max1,
                   max1 * max2 * max3
                   )

    # 14
    def buddy_string(self, A, B):
        # Strings in python are immutable which means we can not change the charachters in-place so I changed them to list
        # So that it becomes easier to work with indexes and swapping the elements
        A1 = list(A)
        B1 = list(B)
        if len(A) != len(B):
            return False
        for i in range(len(A1)):
            A1 = list(A)
            for j in range(i+1, len(A1)):
                # t is the helper variable to handle swapping elements of the list
                t = A1[i]
                A1[i] = A1[j]
                A1[j] = t
                if A1 == B1:
                    return True
        return False

    # 15
    def num_ways(self, m, n):
        # it is done recursively with an exponential time complexity which can be avoided by dynamic programming approach
        if m == 1 or n == 1:
            return 1
        return self.num_ways(m-1, n) + self.num_ways(m, n-1)

    # 16
    def find_first_last(self, nums, target):
        res_arr = []
        for i, num in enumerate(nums):
            if num == target:
                res_arr.append(i)
        if res_arr == []:
            return [-1, -1]
        return [res_arr[0], res_arr[-1]]

    # 18
    def look_and_say(self, nth):
        # 1, 11, 21, 1211, ...
        if nth == 1:
            return "1"
        elif nth == 2:
            return "11"

        s = "11"
        count = 1
        for i in range(3, nth+1):
            s += '$'
            cnt = 1
            tmp = ""
            for j in range(1, len(s)):
                if s[j-1] != s[j]:
                    tmp += str(cnt + 0)
                    tmp += s[j-1]
                    cnt = 1
                else:
                    cnt += 1
            s = tmp
        return s

    # 19
    def climb_the_stairs(self, n):
        # The person can reach nth stair from either (n-1)th stair or from (n-2)th stair
        # So we can write it in recursion
        # Somehow similar to the fibonacci method
        # Time complexity of this method: O(2^n)
        if n <= 2:
            return n
        return self.climb_the_stairs(n-1) + self.climb_the_stairs(n-2)

    # 19
    def climb_the_stairs_dynamic(self, n):
        # Dynamic programming
        # instead of having an exponential time complexity of recursion we achieve the linearO(n)
        # We already know that if the number of stairs is 0 then we have 0 options and so on with 1 and 2
        # So we can build our starting point like following array
        f = [0, 1, 2]
        for i in range(3, n+1):
            f.append(f[i-1] + f[i-2])
        return f[n]

    # 20
    def reverse(self, string):
        print(string)
        rev = str()
        for i in range(1, len(string)):
            rev += string[len(string)-i]
        rev += string[0]
        return rev

    # 21
    def push_dominoes(self, s: str) -> str:
        l=len(s)
        print(s)
        # change the strin to array to be able to exchange values in the array
        arr=[s[i] for i in range(l)]
        # an array that helps to keep track of the changes
        check=[0 for i in range(l)]
        # traverse the array from left to right to check for R's
        for i in range(1,l):
            if arr[i-1]=='R':
                if arr[i]=='.':
                    arr[i]='R'
                    # mark in the check array to be able to handle the R.L situations
                    check[i] = 1
        # traverse the array from the end to check for L's
        for i in range(l-2,-1,-1):
            if arr[i+1]=='L':
                if arr[i]=='.':
                    arr[i]='L'
                elif arr[i]=='R' and s[i]=='.' and check[i] != 1:
                    arr[i]='L'
                else:
                    arr[i] = '.'
        return ''.join(arr)

    # TODO: Better way to do it in O(n^2) needs to be implemented
    # 22
    def find_pythagorean(self, nums):
        # Naive way to solve the problem is to just do it with three loops with the time complexity of O(n^3).
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]*nums[i] == nums[j]*nums[j] + nums[k]*nums[k] or \
                        nums[j]*nums[j] == nums[i]*nums[i] + nums[k]*nums[k] or \
                        nums[k]*nums[k] == nums[j]*nums[j] + nums[i]*nums[i]:
                        print(nums[i], nums[j], nums[k])
                        return True
        return False

    # 23
    def fizzbuzz(self, n):
        r = str()
        for i in range(1,n+1):
            if i >= 5 and i % 3 == 0 and i % 5 == 0:
                r += 'FizzBuzz'
            elif i >= 3 and i % 3 == 0:
                r += 'Fizz'
            elif i >= 5 and i % 5 == 0:
                r += 'Buzz'
            else:
                r += str(i)
        return r

    # 24
    def binary_search(self, nums: list, n: int) -> (str,int):
        first, last = 0, len(nums) - 1
        while first <= last:
            mid = (first + last) // 2
            if n == nums[first]:
                return True, first
            elif n == nums[mid]:
                return True, mid
            elif n == nums[last]:
                return True, last
            elif nums[first] < n <= nums[mid]:
                last = mid - 1
            else:
                first = mid + 1
        return False

    # 27
    def reverse_alphabets(self, S):
        if not S:
            return S
        str_ = ""
        index1 = 0
        index2 = len(S) - 1
        while index1 < len(S):

            if index2 >= 0 and S[index1].isalpha() and S[index2].isalpha():
                str_ += S[index2]
                index2 -= 1
                index1 += 1
            elif S[index1].isalpha():
                index2 -= 1
            elif not S[index1].isalpha():
                str_ += S[index1]
                index1 += 1
            else:
                index2 -= 1
                index1 += 1
        return str_

    # 28
    def is_anagram(self, str1, str2):
        # of course many other ways to solve this problem
        # but I used mapping in python just to remind it and see basically how it functions.
        if str1 == str2:
            return False
        else:
            str1 = list(str1.lower())
            str2 = list(str2.lower())
            str1_map = {x: str1.count(x) for x in str1}
            str2_map = {y: str2.count(y) for y in str2}
            print(str1_map)
            print(str2_map)
            if str1_map == str2_map:
                return True
            else:
                return False

    # 29
    def majority(self, nums):
        # using hash map makes it easy
        # of course several other solutions is appliable for this problem
        print(nums)
        nums_map = {x: nums.count(x) for x in nums}
        max = 0
        print(nums_map)
        for key in nums_map.keys():
            if nums_map[key] > max:
                max = nums_map[key]
        if max > len(nums) // 2:
            return True
        return False

    # 30
    def sort_colors(self, colors):
        print(colors)
        white, red, blue = [], [], []
        for i, cl in enumerate(colors):
            if cl == 0:
                white.append(cl)
            elif cl == 1:
                red.append(cl)
            elif cl == 2:
                blue.append(cl)
            else:
                return False
        colors = white + red + blue
        print(colors)

    # 31
    def power3(self, n):
        while n > 1:
            n = n / 3
        if n == 1:
            return True
        return False

    # 32
    def three_sum(self, nums):
        # The naive algorithm is just go through the list in 3 for loops
        # So the time complexity is obviously O(n^3)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for t in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[t] == 0:
                        print(nums[i], nums[j], nums[t])

    # 32
    def three_sum_eff(self, nums):
        # A bit more wiser idea is that to use a mapping system.
        # Which brings the time complexity down to O(n^2)
        print(nums)
        for i in range(len(nums)):
            s = set()
            # Here we check whether there is any element that is the negation of sum of two other elements
            # Which means that if we sum those three elements it gives us zero.
            for j in range(i+1, len(nums)):
                x = -(nums[i] + nums[j])
                if x in s:
                    print("Found with: ", x, nums[i], nums[j])
                else:
                    s.add(nums[j])

    # 33
    def sum_digits(self, n):
        # Easy way is to use brute force and sum all the digits till it gets less than 10.
        sum = 0
        while n > 0 or sum > 9:
            if n == 0:
                n = sum
                sum = 0
            sum += n % 10
            n //= 10
        return sum

# 6
class MaxStack:
    # simple stack with max functionality. max function has the time complextity of O(1).
    def __init__(self):
        self.stack = []
        # to keep track of the max value in the stack as we do push and pop
        self.trackStack = []
        pass

    def push(self, val):
        self.stack.append(val)
        if len(self.stack) == 1:
            self.trackStack.append(val)
            return
        if val > self.trackStack[-1]:
            self.trackStack.append(val)
        else:
            self.trackStack.append(self.trackStack[-1])

    def pop(self):
        self.stack = self.stack[:-1]
        self.trackStack = self.trackStack[:-1]
        return self.stack

    def max(self):
        print(self.trackStack)
        return self.trackStack[-1]

# Driver code 1: move zeros
# nums = [0,0,0,0,5,0,1,0,0]
# print(Solution().moveZeros(nums))

# Driver code 2: kth largest number
# nums = [1,2,3,4,5,6,0,8,9]
# k = 3
# res: 6
# print(Solution().kth_largest_num(nums, k))

# Driver code 3: single number
# nums = [4, 4, 3, 7, 3, 14, 6, 14, 5, 6, 5]
# print(Solution().find_single(nums))

# Driver code 4: two sum
# nums = [3,2,0,1]
# k = 5
# True
# print(Solution().two_sum(nums, k))
# print(Solution().two_sum_2(nums, k))

# Driver code 5: longest substring
# str = 'aacbcddefff'
# res = 4
# print(Solution().longest_length_substring(str))

# Driver code 6: MaxStack
# s = MaxStack()
# s.push(1)
# s.push(0)
# s.push(6)
# s.push(5)
# print(s.max())
# 5
# s.pop()
# s.pop()
# print(s.max())
# 4

# Driver code 7: balanced parenthesis
# str1 = '(((((((()'
# str2 = '{}'
# print(Solution().balanced_parenthesis(str1))

# Driver code 8: buy and sell
# nums = [9, 11, 8, 5, 7, 10]
# res: 5 (10 - 5)
# print(Solution().buy_and_sell(nums))

# Code driver 9: max subarray sum
# nums = [-4, -5, -2, 1]
# print(Solution().max_subarray_sum(nums))

# Code driver 11: courses to take
# courses = {
#  'CSC300': ['CSC100', 'CSC200'],
#  'CSC200': ['CSC100'],
#  'CSC100': []
# }
# print(Solution().courses_to_take(courses))

# Code driver 12: Edit distance
# Also in this example using recursive function in a class is shown.
# str1 = 'biting'
# str2= 'sitting'
# m = len(str1)
# n = len(str2)
# print(Solution().edit_distance(str1, str2, m, n))

# Code driver 13: maximum product of three elements
# nums  = [-4, -4, 2, 3]
# k = 3
# print(Solution().max_product(nums, k))
# print(Solution().max_product_improved(nums, k))

# Driver code 14: Buddy Strings
# A = 'ab'
# B = 'ba'
# print(Solution().buddy_string(A, B))

# Driver code 15: number of ways
# m = 3
# n = 3
# print(Solution().num_ways(m, n))

# Code driver 16: First and Last Indices of an Element in a Sorted Array
# target = 9
# nums = [1,3,3,5,7,8,9,9,9,15]
# print(Solution().find_first_last(nums, target))

# Code driver 18: Look-and-say sequence
# nth = 4
# 1, 11, 21, 1211, 111221, 312211, ...
# print(Solution().look_and_say(nth))

# Code driver 19: Number of Ways to Climb Stairs
# n = 5
# print(Solution().climb_the_stairs(n))
# print(Solution().climb_the_stairs_dynamic(n))

# Driver code 20: simple reverse
# string = "ALINegin"
# print(Solution().reverse(string))

# Driver code 21: push dominoes
# dominoes = '..R...L..R.'
# print(Solution().push_dominoes(dominoes))

# Driver code 22: Find Pythagorean Triplets
# nums = [7, 33, 56, 65]
# print(Solution().find_pythagorean(nums))

# Driver code 23: FizZBuzZ
# n = 15
# print(Solution().fizzbuzz(n))

# Driver code 24: binary search
# n = 74
# nums = [1, 4, 7, 20, 25, 56, 74, 87]
# print(Solution().binary_search(nums, n))

# Driver code 27: reverse alphabets
# string = 'sea!$hells3'
# sll!$ehaes3
# print(Solution().reverse_alphabets(string))

# Driver code 28: Is Anagram
# str1 = 'cinema'
# str2 = 'iceman'
# print(Solution().is_anagram(str1, str2))

# Driver code 29: majority
# nums = [4, 2, 4]
# print(Solution().majority(nums))

# Driver code 30: Sort colors
# colors = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
# print(Solution().sort_colors(colors))

# Driver code 31: Power3
# n = 81
# print(Solution().power3(n))

# Driver code 32: 3Sum
# nums = [0, -1, 2, -3, 1]
# print(Solution().three_sum(nums))
# print(Solution().three_sum_eff(nums))

# Driver code 32: Sum Digits Until One
n = 987
print(Solution().sum_digits(n))