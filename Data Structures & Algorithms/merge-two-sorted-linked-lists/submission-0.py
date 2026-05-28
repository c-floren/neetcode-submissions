# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # intuition:
        # equal values will be next to each other
        # then compare which next value is less than
        # the other and point to that
        # then unused node will be compared to the next
        # node and placed depending if is less than
        # one linked list might run out first
        # so I need to be able to make sure that
        # if there is still
        # values left in one linked list
        # I add those values
        # I'm thinking of a zig zag approach
        # where I will compare the head
        # I will have to maintain the head of list1
        # in a temporary variable
        # if equal I will point list1 head to list2 head
        
        # this will cover the equal length portion of the LL
        # create output linkedlist
        # dummy node
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
            

