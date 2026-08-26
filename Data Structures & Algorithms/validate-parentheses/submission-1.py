class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        #stack
        for i in range(len(s)):
            if len(l)>0 and ((s[i]==']' and l[len(l)-1]=='[') or (s[i]=='}' and l[len(l)-1]=='{') or (s[i]==')' and l[len(l)-1]=='(')):
                l.pop()
            else:
                l.append(s[i])
            
        return False if (len(l)) else True
