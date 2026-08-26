class Solution:
    def minm(self, selected: dict) -> int:
        minval = 1000000
        minkey = 0
        for key, value in selected.items():
            if minval>value:
                minval = value
                minkey = key
        return [minkey,minval]
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for x in range(len(nums)):
            m[nums[x]] = m.get(nums[x],0)+1
        res = []
        minval = 0
        minkey = 0
        selected = {}
        for key, val in m.items():
            if len(selected)<k:
                #add elements
                selected[key]=val
            else:
                minkey, minval = self.minm(selected)
                if minval<val:
                    del selected[minkey]
                    selected[key]=val
        for key in selected:
            res.append(key)
        return res


