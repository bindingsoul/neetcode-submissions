class Solution:
    def isPalindrome(self, s: str) -> bool:
        #have only alphanumeric characters
        #use two pointer method
        n = len(s)
        i = 0
        j = n-1
        while i<j:
            if s[i].isalnum()==True and s[j].isalnum()==True:
                if s[i].lower()!=s[j].lower():
                    print(s[i]," ", s[j])
                    return False
                i+=1
                j-=1
            elif s[i].isalnum()==True:
                j-=1
            elif s[j].isalnum()==True:
                i+=1
            else:
                i+=1
                j-=1
        return True
            
