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

    return max,l

  def find_single(self, nums):
    # XOR helps to do it very efficient with the space requirement of O(1) and time complexity of O(n)
    # XOR of a number with itself is 0
    # XOR of a number with 0 is the number itself
    res = nums[0]
    # Do XOR of all elements
    for i in range(1, len(nums)):
      res = res ^ nums[i]
    return res

  # driver code: 1
nums = [0,0,0,0,5,0,1,0,0]
print(Solution().moveZeros(nums))

# driver code: 2
nums = [1,2,3,4,5,6,0,8,9]
k = 3
# res: 6
print(Solution().kth_largest_num(nums, k))

# driver code: single number
nums = [4, 4, 3, 7, 3, 14, 6, 14, 5, 6, 5]
print(Solution().find_single(nums))