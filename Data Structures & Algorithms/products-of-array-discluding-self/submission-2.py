class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            result = [0] * len(nums)
            total = 1
            zCount = 0
            for num in nums:
                if num == 0:
                    zCount+=1
                else:
                    total *= num

            for i in range(len(nums)):
                if zCount == 1:
                    if(nums[i] == 0):
                        result[i] = total
                    else:
                        result[i] = 0
                if(zCount == 0):
                    result[i] = int(total/nums[i])
                

            return result
                

                