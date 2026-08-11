class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numsSet = set(nums)

        currLength = 0
        longest = 0
        for num in numsSet:
            currNum = num
            currLength += 1
            if(num - 1 not in numsSet):
                while(currNum + 1 in numsSet):
                    currLength += 1
                    currNum += 1


            if currLength > longest:
                longest = currLength

            currLength = 0

        return longest

