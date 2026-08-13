class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        # Make a map having key and value as lowest integer
        # So find the value
        m = {}
        for x in range(len(nums)):
            if (target-nums[x]) in m:
                return [m[target-nums[x]],x]
            m[nums[x]]=x

