class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        bucket = [[] for x in range(len(nums)+1)]

        for x in range(len(nums)):
            freqmap[nums[x]]=1+freqmap.get(nums[x],0)
        
        for key, val in freqmap.items():
            bucket[val].append(key)

        res = []

        for x in range(len(bucket)-1,0,-1):
            if len(res)==k:
                return res
            if len(bucket[x])!=0:
                res.extend(bucket[x])

        return res
            
