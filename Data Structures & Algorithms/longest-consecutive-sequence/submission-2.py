class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if(len(nums) == 0):
            return 0

        numsSet = set(nums)
        numsList = list(numsSet)
        numsList.sort()

        current = 1
        longest = 1
        for i in range(len(numsList) - 1):
            if(numsList[i+1] - numsList[i] == 1):
                current += 1
            else:
                current = 1
            
            if(current > longest):
                longest = current
        
        return longest

