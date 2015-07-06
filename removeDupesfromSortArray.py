class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
            p1 = 0
            p2 = len(nums)-1
            while p2 > p1:
                if nums[p1] == nums[p1+1]:
                    nums.pop(p1+1)
                    p2 = len(nums)-1
                else:
                    p1 = p1+1
            return len(nums)  