class Solution:
    def reverseBits(self, n: int) -> int:
        flippedBits = format(n, "b")[::-1]
        addedZeros = "0" * (32-len(flippedBits))
        return int(flippedBits + addedZeros,2)