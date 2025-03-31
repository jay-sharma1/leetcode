import re

# This is done to minimize space used in memory.
def isPalindrome(s: str) -> bool:
    leftPointer = 0
    rightPointer = len(s) - 1
    
    leftString, rightString = None, None
    
    # Loop until pointers cross
    while leftPointer <= rightPointer:
        leftString = s[leftPointer]
        rightString = s[rightPointer]
        
        leftIsAlpha = re.match(r"[A-Za-z0-9]", leftString)
        rightIsAlpha = re.match(r"[A-Za-z0-9]", rightString)

        # If left string is not an alphanumeric, move pointer to the right.
        if not leftIsAlpha:
            leftPointer += 1
        
        # If right string is not an alphanumeric, move pointer to the left.
        if not rightIsAlpha:
            rightPointer -= 1
        
        # If both are alphanumerics, compare the strings
        if leftIsAlpha and rightIsAlpha:
            if leftString.lower() != rightString.lower():
                return False
            else:
                leftPointer += 1
                rightPointer -= 1
    
    return True

# Test
print(isPalindrome(s = " "))