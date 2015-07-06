class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        nums2 = nums[:]
        nums2.sort()
        for i in range(0,len(nums2)):
            if target-nums2[i] in nums2:
                if i != nums2.index(target-nums2[i]):
                    f1 = nums.index(nums2[i])
                    f2 = nums.index(target-nums2[i])
                    if f1 == f2:
                        nums.pop(f1)
                        f2 = nums.index(target-nums2[i])+1
                    if f1> f2:
                        return(f2+1,f1+1)
                    else:
                        return(f1+1,f2+1)