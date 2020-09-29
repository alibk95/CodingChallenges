class Solution:
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

    def find_single(self, nums):
        # XOR helps to do it very efficient with the space requirement of O(1) and time complexity of O(n)
        # XOR of a number with itself is 0
        # XOR of a number with 0 is the number itself
        res = nums[0]
        # Do XOR of all elements
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res

    def two_sum(self, nums, k):
        # [4,7,1,-3,2]
        for i in range(len(nums)):
            nums[i] = nums[i] - k
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == 0:
                    return True
        return False

    def two_sum_2(self, nums, k):
        # More pythonic way of doing it
        for i in range(0, len(nums)):
            if k - nums[i] in nums:
                return True
        return False

    def longest_length_substring(self, str):
        longest = 0
        aux = []
        for s in str:
            if s in aux:
                aux = aux[aux.index(s) + 1:]
            aux.append(s)
            longest = max(longest, len(aux))
        return longest

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

    def buy_and_sell(self, nums):
        max = nums[1] - nums[0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] > max:
                    max = nums[j] - nums[i]
        return max

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

# Driver code: move zeros
# nums = [0,0,0,0,5,0,1,0,0]
# print(Solution().moveZeros(nums))

# Driver code: kth largest number
# nums = [1,2,3,4,5,6,0,8,9]
# k = 3
# res: 6
# print(Solution().kth_largest_num(nums, k))

# Driver code: single number
# nums = [4, 4, 3, 7, 3, 14, 6, 14, 5, 6, 5]
# print(Solution().find_single(nums))

# Driver code: two sum
# nums = [3,2,0,1]
# k = 5
# True
# print(Solution().two_sum(nums, k))
# print(Solution().two_sum_2(nums, k))

# Driver code: longest substring
# str = 'aacbcddefff'
# res = 4
# print(Solution().longest_length_substring(str))

# Driver code: MaxStack
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

# Driver code: balanced parenthesis
# str1 = '(((((((()'
# str2 = '{}'
# print(Solution().balanced_parenthesis(str1))

# Driver code: buy and sell
# nums = [9, 11, 8, 5, 7, 10]
# res: 5 (10 - 5)
# print(Solution().buy_and_sell(nums))

# Code driver: max subarray sum
# nums = [-4, -5, -2, 1]
# print(Solution().max_subarray_sum(nums))

# Code driver: courses to take
# courses = {
#  'CSC300': ['CSC100', 'CSC200'],
#  'CSC200': ['CSC100'],
#  'CSC100': []
# }
# print(Solution().courses_to_take(courses))

# Code driver: Edit distance
# Also in this example using recursive function in a class is shown.
# str1 = 'biting'
# str2= 'sitting'
# m = len(str1)
# n = len(str2)
# print(Solution().edit_distance(str1, str2, m, n))

# Code driver:
nums  = [-4, -4, 2, 3]
k = 3
print(Solution().max_product_improved(nums, k))