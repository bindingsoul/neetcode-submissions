class Solution:
    def validPalindrome(self, s: str) -> bool:
        #in  palindrom sequence.
        #if we add a new char, and we get a non-palindrome
        #that means that char, paried up with something 
        # unlike. So we need to remove the character again.
        # thinking the reverse, if we have a unlike pair,
        # we need to remove either of this character 
        # and check for palindrom or not.

        res = True

        n = len(s)
        i = 0
        j = n-1
        while(i<j):
            if s[i]!=s[j]:
                break
            i+=1
            j-=1
        ii = i
        jj = j
        i+=1
        while(i<j):
            if s[i]!=s[j]:
                res = False
                break
            i+=1
            j-=1
        jj-=1
        if res==True:
            return True
        while(ii<jj):
            if s[i]!=s[j]:
                res = False
                break
            ii+=1
            jj-=1
        
        return res
        