# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        if n == len(nodes):
            return nodes[1]
        elif n == 1:
            nodes[-2].next = None
            return nodes[0]
        else:
            nodes[-n-1].next = nodes[-n+1]
            return nodes[0]
        