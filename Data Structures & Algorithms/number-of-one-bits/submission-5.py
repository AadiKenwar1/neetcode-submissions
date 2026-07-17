class Solution:
    def hammingWeight(self, n: int) -> int:
        if(n == 0):
            return 0
        initPlace = int(math.log(n,2))
        result = 0
        binaryStr = ""
        while(initPlace >= 0):
            placeValue = 2**initPlace
            if(placeValue <= n):
                result += 1
                n -= placeValue
            initPlace -= 1
        return result