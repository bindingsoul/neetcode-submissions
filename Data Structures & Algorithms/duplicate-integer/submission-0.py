class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d1 = {}
        for x in nums:
            if x in d1:
                return True
            else:
                d1[x] = 1
        return False