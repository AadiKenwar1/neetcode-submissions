class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordMap = {} #key -> charMap : value -> str list
        for i in range(len(strs)):
            key = [0] * 26
            for char in strs[i]:
                idx = ord(char) - ord('a')
                key[idx] = key[idx] + 1

            keyString = str(key)
            print(keyString)
            if(keyString in wordMap):
                wordMap.get(keyString).append(strs[i])
            else:
                wordMap[keyString] = [strs[i]]
            key = [0] * 26
        return list(wordMap.values())