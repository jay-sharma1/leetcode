def productExceptSelf(nums: list[int]) -> list[int]:
    prefix = [1] * len(nums)
    postfix = [1] * len(nums)

    # Prefix array will contain the product of every number before num[i], including num[i] 
    for ind, num in enumerate(nums):
        if ind == 0:
            # Base case, first element in prefix is same as first element in num
            prefix[ind] = num
        else:
            # Each element in prefix is the product of the current num and previous element in prefix
            prefix[ind] = num * prefix[ind - 1]
        
    # Postfix array will contain the product of every number after num[i], including num[i] 
    # Must traverse nums and postfix in reverse order
    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) -1:
            # Base case, last element in postfix is same as last element in nums
            postfix[i] = nums[i]
        else:
            # Each element in postfix is the product of the current num and next element in postfix
            postfix[i] = nums[i] * postfix[i + 1]
            
    
    output = [1] * len(nums)
    
    # Populate output array. Output[i] is the product of prefix[i - 1] and postfix[i + 1]
    for i in range(0, len(nums)):
        if i == 0:
            # Base case for first element in output, since [i - 1] will be outisde of bounds in prefix
            output[i] = postfix[i + 1]
        elif i == len(nums) - 1:
             # Base case for last element in output, since [i + 1] will be outside of bounds in postfix
            output[i] = prefix[i - 1]
        else:
            output[i] = prefix[i - 1] * postfix[i + 1]
    
    return output

# Testing
print(productExceptSelf([1,2,4,6]))
print(productExceptSelf([-1,0,1,2,3]))
        
    
