# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret_head = ListNode(0, None)
        curr_node = ret_head
        carry = 0
        while l1 or l2:
            if l1 and l2:
                val = carry + l1.val + l2.val
                if val > 9:
                    val -= 10
                    carry = 1
                    curr = ListNode(val, None)
                else:
                    carry = 0
                    curr = ListNode(val, None)
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                val = l1.val + carry
                if val > 9:
                    val -= 10
                    carry = 1
                    curr = ListNode(val, None)
                else:
                    carry = 0
                    curr = ListNode(val, None)
                l1 = l1.next
            elif not l1 and l2:
                val = l2.val + carry
                if val > 9:
                    val -= 10
                    carry = 1
                    curr = ListNode(val, None)
                else:
                    carry = 0
                    curr = ListNode(val, None)
                l2 = l2.next
            curr_node.next = curr
            curr_node = curr
        if carry:
            curr_node.next = ListNode(1, None)
        return ret_head.next


                

        