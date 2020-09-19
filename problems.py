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
    e = 0
    l = []
    for j in range(k):
      t = 0
      for i in range(len(nums)):
        if nums[i] > e:
          t = nums[i]

        nums[i] = 0

    return t,l

# driver code: 1
nums = [0,0,0,0,5,0,1,0,0]
print(Solution().moveZeros(nums))

# driver code: 2
nums = [3, 5, 7, 8, 9, 2]
k = 3
# res: 6
print(Solution().kth_largest_num(nums, k))


