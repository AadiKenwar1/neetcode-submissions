class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numSet = set(nums)
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                added = nums[i] + nums[j]
                thirdNum = added * -1
                foundTriple = [nums[i], nums[j], thirdNum]
                foundTriple.sort()
                if(i == j):
                    continue
                if(thirdNum not in numSet):
                    continue
                if(nums.index(thirdNum) == i or nums.index(thirdNum) == j):
                    continue
                if(foundTriple in result):
                    continue
                result.append(foundTriple)

        return result






