def dailyTemperatures(temperatures: list[int]) -> list[int]:
    result = [0] * len(temperatures)
    stack = []
    
    # Iterate through temperatures backwards
    for ind in range(len(temperatures) - 1, -1, -1):
        # The temperature value in temperatures at our current index
        currentVal = temperatures[ind]
        
        # Stack is filled with indexes. Stackval is the temp value assosiated with the index on top of the stack
        stackVal = float('inf')
        if len(stack) > 0:
            stackVal = temperatures[stack[-1]]
        
        # While stack is not empty and current value is greater than top value of stack
        # keep popping values until the stack is empty or stack val is greater than current val.
        while len(stack) > 0 and currentVal >= stackVal:
            stack.pop()
            if len(stack) > 0:
                stackVal = temperatures[stack[-1]]
        
        if not stack:
            # If stack is empty, add the current value's index onto the stack
            result[ind] = 0
        else:
            # Stack value is higher than current value, so set the corresponding index in results to equal the 
            # difference in stack top index and current index.
            result[ind] = stack[-1] - ind

        # Since the current value is smaller than top of stack, add its index to the stack.
        stack.append(ind)
        
    return result

                
                    
#Test
print(dailyTemperatures(temperatures=[89,62,70,58,47,47,46,76,100,70]))
