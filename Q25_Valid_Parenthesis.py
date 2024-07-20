class Solution:
    def isValid(self, s: str) -> bool:
        # have a stack 
        # for every char in stack, if its an opening one add it to stack, 
        # if its a closing one, pop from stack - store it in temporary
        # if closing character type doesnt match type of temp, return False 
        # keep going, if at the end stack is empty return true, else false

        stack = []
        closeToOpen = {'(':')', '[':']', '{':'}'}
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if len(stack) == 0: return False
                top = stack.pop()
                if closeToOpen[top] != char:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False