# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # basically just initializing a list with a 0 node
        result = ListNode()
        # set tail = to that list so we can go through
        tail = result
        # while both input lists exist
        while list1 and list2:
            # find if list1 or list2 has next lowest value
            if list1.val <= list2.val:
                # if it does, then we assign our tail's next node = list1
                # then update list1 to its next node
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # we need to update tail to move to next node
            tail = tail.next
        # since the lists can be different sizes, list1 or list2 
        # could have a some left over nodes
        if list1:
            # if list1 has some left over, we can just set tail.next equal to the rest of list1 nodes
            # This works since list1 is already sorted and list2 is empty
            tail.next = list1
        elif list2:
            tail.next = list2
        # we have to return result.next bc we initialized result with that dummy node
        return result.next