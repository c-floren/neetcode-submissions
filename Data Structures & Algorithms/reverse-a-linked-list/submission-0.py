# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointers
        # curr set to first node (head)
        # prev set to null (initially)
        # curr next pointer set to prev
        # prev shifted to curr
        # curr shifted to next node
        # set curr next to prev
        # do it again until curr is null
        # return new head which is now prev

        prev, curr = None, head

        while curr:
            # temporary to save actual next value
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
