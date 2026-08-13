class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        word1 = strs[0]
        for i,w in enumerate(word1):
            for s in strs:
                if s[i]!=w:
                    return res
            res+=w
        return res
            