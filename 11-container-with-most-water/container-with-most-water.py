class Solution(object):
    def maxArea(self, height):
        n=len(height)
        left=0
        area=-1
        right=n-1      
        while(left<right):
            width=right-left
            h=min(height[left],height[right])
            area=max(area,width*h)
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return area