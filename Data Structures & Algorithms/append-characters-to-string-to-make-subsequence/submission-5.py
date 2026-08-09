class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
    

#current: c, a, t
#i: 1, 2, 3, 4
#j: 1, 2
# s = caaat
# t = cat
#     01234567


        i = 0
        j = 0
        current = ''
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1
            i += 1
        return len(t) - j

        return len(t) - j
        

