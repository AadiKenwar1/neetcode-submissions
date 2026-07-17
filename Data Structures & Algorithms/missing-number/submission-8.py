class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #inputSet = set(nums)
        #totalSet = set()
        #for i in range(len(nums) + 1):
        #    totalSet.add(i)
        #return (inputSet ^ totalSet).pop()
        
        totalSum = 0
        inputSum = 0
        for i in range(len(nums) + 1):
            totalSum += i
            if(len(nums) != 0):
                inputSum += nums.pop(0)
        return totalSum - inputSum

        