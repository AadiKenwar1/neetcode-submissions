class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = str(format(n, "b"))
        result = 0;
        for char in binary:
            if char == '1':
                result+=1
        return result