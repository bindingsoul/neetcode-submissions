class Solution:
    def minm(self, m: dict, k: int) -> int:
        minval = 1000000
        minkey = 0
        for key, value in m.items():
            if k!=0 and minval>value:
                minval = value
                minkey = key
                k-=1
            else:
                break
        return [minkey,minval]
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for x in range(len(nums)):
            if nums[x] not in m:
                m[nums[x]]=1
            else:
                m[nums[x]]+=1
        res = []
        minval = 0
        minkey = 0
        x = 0
        for key, val in m.items():
            he =  self.minm(m,k)          
            minkey = he[0]
            minval = he[1]    
            if val > minval:
                minval = val
                m[minkey]=-1

        for key in m:
            if m[key]!=-1:
                res.append(key)
        return res


