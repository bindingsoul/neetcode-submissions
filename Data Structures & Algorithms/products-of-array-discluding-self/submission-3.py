class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1 for i in range(len(nums)+1)]
        p[1]=nums[0]
        c = 0
        res = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
                val = i
        if c==0:
            for i in range(len(nums)):
                p[i]=p[i-1]*nums[i]
        
            for i in range(len(nums)):
                res[i]= p[i-1]*(p[len(nums)-1]//p[i])
            return res
        if c==1:
            q = 1
            for i in range(len(nums)):
                if nums[i]!=0:
                    q = q*nums[i]
            res[val]=q
            return res
        if c>1:
            return res
                    
        
        

        
        
        # if we have more than 1 zero the answer is zero all over
        # if we have only 1 zero than the answer is non zero product at the product

