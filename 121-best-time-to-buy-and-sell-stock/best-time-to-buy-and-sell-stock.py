class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max=0
        min=prices[0]
        for i in range(len(prices)):
            if(prices[i]<min):
                min=prices[i]
            if(prices[i]-min>max):
                max=prices[i]-min
        return max