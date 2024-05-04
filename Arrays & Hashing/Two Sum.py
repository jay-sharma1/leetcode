# This is the brute force method, where for each element in the array, we iterate over every element after it until we find a sum. This is O(n**2)
def twoSumBrute(nums: list[int], target: int) -> list[int]:
    for ind1, num1 in enumerate(nums):
        for ind2 in range(ind1 + 1, len(nums)):
            if num1 + nums[ind2] == target:
                return [ind1, ind2]
            

# Another option is to iterate over the array once, and while we do that every element is added to a hashtable.
# Then check if target - current is present in the table, if it is then we have a proper result.
# This results in higher space complexity, but lower time complexity of O(n).

def twoSumHash(nums: list[int], target: int) -> list[int]:
    HashMap = {}
    
    for ind, currentNum in enumerate(nums):
        if (target - currentNum) in HashMap:
            return [ind, HashMap[target - currentNum]]
        
        HashMap[currentNum] = ind
        


print(twoSumBrute([3,2,4], 6))
print(twoSumHash([3,2,4], 6))
