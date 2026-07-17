class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        inputSet = set(nums)
        outputSet = set()
        for i in range(len(nums) + 1):
            outputSet.add(i)
        return (inputSet ^ outputSet).pop()
        

        