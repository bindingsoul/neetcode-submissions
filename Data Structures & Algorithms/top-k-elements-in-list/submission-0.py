class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for x in range(len(nums)):
            if nums[x] not in m:
                m[nums[x]]=1
            else:
                m[nums[x]]+=1
        res = []
        minval = 100000
        minkey = 0
        x = 0
        for key, val in m.items():
            if x<k:
                if minval>val:
                    minval = val
                    minkey = key
                x+=1
                
            else:
                if val > minval:
                    minval = val
                    m[minkey]=-1

        for key in m:
            if m[key]!=-1:
                res.append(key)
        return res


