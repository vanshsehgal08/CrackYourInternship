'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        mod = 10**9 + 7
        def linkedListToNumber(head):
            num = 0
            while head:
                num = (num * 10 + head.data)% mod
                head = head.next
            return num

        num1 = linkedListToNumber(first)
        num2 = linkedListToNumber(second)
        return (num1 * num2)% mod