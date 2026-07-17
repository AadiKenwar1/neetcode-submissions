class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        yogurt_set = set(nums)
        print(yogurt_set)
        yogurt = {}
        for num in nums:
            if (yogurt.get(num) == None):
                yogurt[num] = 1
            else:
                yogurt[num] += 1
                if yogurt[num] == 2:
                    yogurt_set.remove(num)
        return yogurt_set.pop()