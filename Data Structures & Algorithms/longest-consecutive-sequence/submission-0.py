class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = sorted(nums)
        for j in range(len(nums)):
            count = 1
            start = nums[j]
            for i in range(j+1,len(nums)):
                if (start+1)==nums[i]:
                    count+=1
                    start = nums[i]
            res = max(res, count)
            
        return res


