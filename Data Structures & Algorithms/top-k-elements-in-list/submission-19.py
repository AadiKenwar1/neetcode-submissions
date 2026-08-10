class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        result = []
        for num in nums:
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1

        array = list(numMap.items())
        array = sorted(array, key = lambda value: value[1], reverse=True)
        
        for i in range(k):
            result.append(array[i][0])

        return result