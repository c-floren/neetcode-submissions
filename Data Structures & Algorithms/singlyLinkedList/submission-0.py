# Singly Linked List Node
class ListNode:
    # Node: Data stores val and pointer points to next node
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
class LinkedList:
    
    def __init__(self):
        # Dummy Node allows us to...
        # Assume LL not empty
        # We ignore default value
        # Real head of the node would be the head.next

        self.head = ListNode(-1)
        self.tail = self.head
        # When LL empty (only dummy exists) => head = tail

    
    def get(self, index: int) -> int:
        curr = self.head.next # could be empty (None)
        i = 0
        while curr: # LL not empty
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1 # index out of bounds/list is empty

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val) # create node with val
        new_node.next = self.head.next # new node points to real head node
        self.head.next = new_node
        if not new_node.next: # if LL empty before inserting
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val) # tail points to new val, appending val
        # tail is still equal to head
        self.tail = self.tail.next # moves tail to new val

    def remove(self, index: int) -> bool:
        # reference to pointer before node to be deleted
        curr = self.head
        i = 0
        # move curr to node before target node
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            # if deleting the last node set tail to node before
            if curr.next == self.tail:
                self.tail = curr
            # skip target
            curr.next = curr.next.next
            return True
        return False     


    def getValues(self) -> List[int]:
        curr = self.head.next
        result = []

        # traverse linkedlist add each val to result list
        while curr:
            result.append(curr.val)
            curr = curr.next

        return result
        
