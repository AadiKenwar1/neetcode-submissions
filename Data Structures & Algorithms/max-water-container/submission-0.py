class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max = 0
        
        while(left < right): 
            currWater = (right - left) * min(heights[left], heights[right])
            
            if currWater > max:
                max = currWater

            if heights[left] < heights[right]: 
                left += 1 
            else: 
                right -=1
        
        return max
