class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        sIdx = 0
        tString = ""

        for i in range(len(t)):
            if sIdx < len(s) and t[i] == s[sIdx]:
                sIdx += 1
                tString += t[i]
        if(s == tString):
            return True
        return False
            

