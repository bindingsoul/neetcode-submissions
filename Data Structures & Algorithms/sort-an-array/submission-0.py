class Solution:
    def merge(self, list1: List[int], list2: List[int]) -> List[int]:
        res = []
        ll1 = len(list1)
        ll2 = len(list2)
        i = 0
        j = 0
        while i <ll1 and j<ll2:
            if list1[i]==list2[j]:
                res.append(list1[i])
                res.append(list2[j])
                i+=1
                j+=1
                continue
            if list1[i]>list2[j]:
                res.append(list2[j])
                j+=1
                continue
            if list1[i]<list2[j]:
                res.append(list1[i])
                i+=1
                continue
        if i<ll1 or j<ll2:
            if i<(ll1):
                res.extend(list1[i:])
            if j<(ll2):
                res.extend(list2[j:])
        return res


    def sortArray(self, nums: List[int]) -> List[int]:
        # we need to write merge sort algorithm
        #merge sort
        #divide and conquer
        # divide the array into two equal parts
        # sort them 
        # merge the sorted array
        # so we need two functions
        # merge and sort

        l = len(nums)
        mid = l//2
        if len(nums)<=1:
            return nums
        list1 = self.sortArray(nums[:mid])
        list2 = self.sortArray(nums[mid:])
        ans = self.merge(list1, list2)
        return ans

        