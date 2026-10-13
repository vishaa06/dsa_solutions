class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        if(n<2):
            return []
        
        Map={}
        for i in range(n):
            val=target-nums[i]
            if(val in Map):
                return[Map[val],i,]
            Map[nums[i]]=i
        
        return []

        
        