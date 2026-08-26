class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i!=j:
                    product = nums[j]*product
            res[i]=product

        return res