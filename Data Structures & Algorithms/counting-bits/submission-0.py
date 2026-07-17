class Solution:
    def countBits(self, n: int) -> List[int]:
        array = []
        for i in range(n + 1):
            iToBinary = format(i, "b")
            numOfOnes = 0
            for char in iToBinary:
                if char == '1':
                    numOfOnes += 1
            array.append(numOfOnes)
        print(array)
        return array

            
            
