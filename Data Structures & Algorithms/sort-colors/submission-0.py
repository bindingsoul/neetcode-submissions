class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l0 = 0
        l1 = 0
        l2 = 0
        for x in range(len(nums)):
            if nums[x]==0:
                l0+=1
            elif nums[x]==1:
                l1+=1
            elif nums[x]==2:
                l2+=1
        x = 0
        while l0:
            nums[x]=0
            l0-=1
            x+=1
        while l1:
            nums[x]=1
            l1-=1
            x+=1

        while l2:
            nums[x]=2
            l2-=1
            x+=1

        