class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        init = 0
        for num in nums:
            init = num ^ init
            
        return init