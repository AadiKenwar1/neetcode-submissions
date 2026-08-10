class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        longest = -1
        initMap = {}
        for i in range(len(s)):
            if s[i] in initMap:
                if (i - initMap[s[i]]-1) > longest:
                    longest = i - initMap[s[i]]-1
            else:
                initMap[s[i]] = i
        return longest
                
