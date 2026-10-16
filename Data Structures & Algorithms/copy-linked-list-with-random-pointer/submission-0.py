from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # Step 1: Create duplicate nodes interwoven with the original list
        curr = head
        while curr:
            cloned = Node(curr.val, curr.next)
            curr.next = cloned
            curr = cloned.next

        # Step 2: Assign random pointers for cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Unweave the two lists
        curr = head
        cloned_head = head.next
        while curr:
            cloned = curr.next
            curr.next = cloned.next
            if cloned.next:
                cloned.next = cloned.next.next
            curr = curr.next

        return cloned_head