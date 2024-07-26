class Solution:
    
    def evaluatePostfix(self, S):
        stack = []
        
        for char in S:
            if char.isdigit():
                stack.append(int(char))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                
                if char == '+':
                    stack.append(op1 + op2)
                elif char == '-':
                    stack.append(op1 - op2)
                elif char == '*':
                    stack.append(op1 * op2)
                elif char == '/':
                    stack.append(int(op1 / op2))  # Perform integer division
        
        return stack[0]