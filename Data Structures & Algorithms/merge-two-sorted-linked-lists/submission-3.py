# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def count(self, list1: Optional[ListNode]) -> int:
        ans = 0
        curr = list1
        while curr:
            curr = curr.next
            ans+=1
        return ans
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.count(list1)
        l2 = self.count(list2)
        res = ListNode()
        head = res
        i = list1
        j = list2
        while i and j:
            if i.val==j.val:
                res.next = ListNode(i.val)
                res = res.next
                res.next = ListNode(j.val)
                res = res.next
                i = i.next
                j = j.next
                l1-=1
                l2-=1
            if i.val<j.val:
                res.next = ListNode(i.val)
                res = res.next
                i=i.next
                l1-=1
            else:
                res.next = ListNode(j.val)
                res = res.next
                j=j.next
                l2-=1

        if i==j:
            return head
        if j:
            while(i):
                res.next = ListNode(i.val)
                res = res.next
                i = i.next
        if i:
            while(j):
                res.next = ListNode(j.val)
                res = res.next
                j = j.next

        return head

























        