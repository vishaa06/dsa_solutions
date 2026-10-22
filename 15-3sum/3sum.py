class Solution(object):
    def threeSum(self, nums):
        n=len(nums)
        answer=set()
        if(n<3):
            return []
        for i in range(n):
            seen=set()
            for j in range(i+1,n):
                k=-(nums[i]+nums[j])
                if(k in seen):
                    answer.add(tuple(sorted([nums[i],nums[j],k])))
                seen.add(nums[j])

        return [list(x) for x in answer]     