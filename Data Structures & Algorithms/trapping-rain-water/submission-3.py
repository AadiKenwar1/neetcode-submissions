class Solution:
    def trap(self, height: List[int]) -> int:
        
        result = 0

        leftStack = []
        rightStack = []
        leftMax = 0
        rightMax = 0

        for i in range(len(height)):
            #Pointers
            left = i
            right = len(height) - 1 - i
            #Monotonic Stack Creation
            leftStack.append(leftMax)
            rightStack.append(rightMax)
            #Checking New Maxes
            if(height[i] > leftMax):
                leftMax = height[left]
            if(height[len(height) - 1 - i] > rightMax):
                rightMax = height[right]

        rightStack.reverse()

        for i in range(len(height)):
            space = max(min(leftStack[i], rightStack[i]) - height[i], 0)
            result += space

        return result
            


