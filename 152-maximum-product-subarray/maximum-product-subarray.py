class Solution(object):
    def maxProduct(self, nums):
        n=len(nums)
        prod=nums[0]
        pre=1
        suff=1
        for i in range(n):
            pre *= nums[i]
            suff *=nums[n-i-1]
            
            prod=max(prod,max(pre,suff))

            if(pre == 0):
                pre=1
            if(suff==0):
                suff=1
        return prod