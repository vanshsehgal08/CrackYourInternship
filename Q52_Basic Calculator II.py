class Solution:
    def calculate(self, s: str) -> int:
        # Initialize variables
        stack = []
        current_number = 0
        current_operation = '+'
        i = 0
        n = len(s)
        
        while i < n:
            char = s[i]
            
            if char.isdigit():
                # Build the current number
                current_number = current_number * 10 + int(char)
            
            # Process the number and operator
            if char in '+-*/' or i == n - 1:
                if char in '+-*/' or char == ' ' or i == n - 1:
                    if current_operation == '+':
                        stack.append(current_number)
                    elif current_operation == '-':
                        stack.append(-current_number)
                    elif current_operation == '*':
                        stack[-1] = stack[-1] * current_number
                    elif current_operation == '/':
                        stack[-1] = int(stack[-1] / current_number)  # Integer division truncates towards zero
                    
                    # Update the current operation
                    current_operation = char
                    # Reset the current number
                    current_number = 0
            
            i += 1
        
        return sum(stack)
