
class TwoStacks:
    def __init__(self):
        self.size = 100  # Assuming a fixed size for simplicity
        self.arr = [None] * self.size
        self.top1 = -1
        self.top2 = self.size

    # Function to push an integer into stack 1
    def push1(self, x):
        # Check if there's space available for stack 1
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            return -1

    # Function to push an integer into stack 2
    def push2(self, x):
        # Check if there's space available for stack 2
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            return -1

    # Function to remove an element from top of stack 1
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            return -1

    # Function to remove an element from top of stack 2
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            return -1