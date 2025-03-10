def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    
    numsSet = set(nums)
    longestSequence = 1
    
    for num in numsSet:
        # A number is only considered the start of a sequence if (number - 1) does not
        # exist in the list. (e.g., [1, 3, 4, 5], 4 cannot be the start since 3 exists in the list)
        if (num - 1) not in numsSet:
            # This number is the start of a sequence
            result = findSequenceLength(numsSet, num)
            
            if result > longestSequence:
                longestSequence = result
    
    return longestSequence
            
        
def findSequenceLength(nums: {int}, start: int):
    # Given the set of numbers and the starting number, find the longest sequence length
    counter = 1
    currentNum = start

    while counter <= len(nums):
        if (currentNum + 1) in nums:
            counter += 1
            currentNum += 1
        else:
            break
    
    return counter

# Test
print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))