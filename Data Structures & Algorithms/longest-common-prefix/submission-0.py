class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        base = strs[0]
        if len(strs)==0:
            return ""
        for i in range(0,len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return result  
            result+= base[i]
        return result