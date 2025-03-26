def generateParenthesis(n: int) -> list[str]:
    # We must always start with an open parantheses
    currentStack = "("
    
    # Keep track of how many open and closed parentheses we have left
    open = n - 1
    close = n
    
    return recursiveParenthesis(open, close, currentStack)
    

def recursiveParenthesis(open: int, close: int, currentStack: str) -> list[str]:
    # Base case: We've used all parentheses, so return the current stack as a list
    if open == 0 and close == 0:
        return [currentStack]
    
    # Now we have two options. Either add an open parentheses or closed parentheses.
    # An open parentheses can be added at any time, but a closed parentheses can only be added if there
    # is already an open parentheses previously in the stack. This can be checked through close > open.
    # The result will be a list of strings with len >= 1
    result1 = []
    if open > 0: 
        result1 = recursiveParenthesis(open - 1, close, currentStack + "(")
    
    result2 = []
    if close > open:
        result2 = recursiveParenthesis(open, close - 1, currentStack + ")")

    # Combine the final string from both results and return it.
    result1.extend(result2)
    return result1
    
    
    
# Test
print(generateParenthesis(n=3))
