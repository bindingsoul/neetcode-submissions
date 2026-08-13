class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for x in range(2*n):
            if x<n:
                ans[x]=nums[x]
            else:
                ans[x]=nums[x-n]
        return ans