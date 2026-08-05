class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = set(nums)
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashset:
                if(nums.index(difference) != i):
                    result = [i, nums.index(difference)]
                    result.sort()
                    return result
        return [0,0]