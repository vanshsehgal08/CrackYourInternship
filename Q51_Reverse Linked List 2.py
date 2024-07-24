# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        leftPrev=dummy
        curr=head

        #   1) reach node at position left
        for i in range(left-1):
            leftPrev=curr
            curr=curr.next
        
        #  Now curr= left and leftprev=node before left
        #  2) reverse from left to right

        prev=None
        for i in range(right-left+1):
            tempNext=curr.next
            curr.next=prev
            prev=curr
            curr=tempNext

        # 3) update ptrs
        leftPrev.next.next=curr # curr is node after right
        leftPrev.next=prev

        return dummy.next

