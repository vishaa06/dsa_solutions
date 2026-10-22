class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum=nums[0]
        n=len(nums)
        for i in range(1,n):
            if(minimum>nums[i]):
                minimum=nums[i]
        return minimum
