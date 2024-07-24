class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the starting point
        dummy = ListNode()
        # Pointer to build the new sorted list
        current = dummy

        # Pointers for list1 and list2
        ptr1 = list1
        ptr2 = list2

        # Merge lists while both pointers are not None
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val <= ptr2.val:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next
            current = current.next

        # If there are remaining nodes in list1
        if ptr1 is not None:
            current.next = ptr1
        # If there are remaining nodes in list2
        if ptr2 is not None:
            current.next = ptr2

        # Return the next node of dummy, which is the head of the merged list
        return dummy.next
