class Solution:
    def reverse_list(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def compute(self, head):
        if not head:
            return None
        
        # Step 1: Reverse the linked list
        head = self.reverse_list(head)
        
        # Step 2: Traverse the reversed list and keep nodes which are greater than or equal to the max seen so far
        max_node = head
        current = head
        
        while current and current.next:
            if current.next.data < max_node.data:
                current.next = current.next.next
            else:
                current = current.next
                max_node = current
        
        # Step 3: Reverse the list back to its original order
        head = self.reverse_list(head)
        
        return head