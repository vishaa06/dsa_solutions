class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        for i in range(n):
            if(target == nums[i]):
                return i
        return -1
        