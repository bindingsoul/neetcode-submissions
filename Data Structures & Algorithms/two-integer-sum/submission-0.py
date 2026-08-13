class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for x in range(l):
            for y in range(x+1,l):
                if target-nums[x]==nums[y]:
                    return [x,y]