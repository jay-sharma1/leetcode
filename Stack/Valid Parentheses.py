brackets = {
    ')': '(',
    ']' : '[',
    '}' : '{' 
}

def isValid(s: str) -> bool:
    characters = list(s)
    stack = []

    for character in characters:
        if character in {'(', '[', '{'}:
            stack.append(character)
        else:
            if len(stack) > 0 and stack[-1] == brackets[character]:
                stack.pop()
            else:
                return False
        
    if len(stack) == 0:
        return True
    else:
        return False

# Test
print(isValid("[]"))
print(isValid("([{}])"))
print(isValid("[(])"))