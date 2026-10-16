# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [1, 2, 3, 4]
# temp [2, 3]
# curr.next [None, 1]
# prev [1, 2]
# curr [2, 3]
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev # None
            prev = curr # 
            curr = temp
        return prev