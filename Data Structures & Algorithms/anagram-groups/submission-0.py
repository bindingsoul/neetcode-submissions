class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        m = {}

        for word in strs:
            w = "".join(sorted(word))
            if w not in m:
                
                m[w]=[word]
            else:
                m[w].append(word)
        
        res = []
        for value in m.values():
            l = list(value)
            res.append(l)

        return res
            