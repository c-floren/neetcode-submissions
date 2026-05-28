# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # intuition
        # the reordered list follows the pattern
        # starts at the first index
        # followed by the last
        # continuously moving inward
        # comes from beginning of the LL
        # then the end of the LL
        # I need to find the tail node
        # Keep track of previous
        # keep track of actual head.next
        # when placing head.next to tail
        # and then change tail to prev
        # I know I finished reordering when I reach the 
        # middle of the linked list
        # fast and slow pointer will make slow pointer reach
        # middle 
        # dont have to actually return anything
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # second half od the list has to be reversed
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2