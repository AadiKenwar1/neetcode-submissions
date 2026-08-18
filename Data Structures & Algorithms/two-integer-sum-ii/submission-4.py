class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numSet = set(numbers)

        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in numSet:
                numIdx = i + 1
                diffIdx = numbers.index(difference) + 1
                print()
                print(numbers[i])
                print(difference)
                print(numIdx)
                print(diffIdx)              
                if numIdx != diffIdx:
                    result = [numIdx, diffIdx]
                    result.sort()
                    return result

        return [0, 0]

