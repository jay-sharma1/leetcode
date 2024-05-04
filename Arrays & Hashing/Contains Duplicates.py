# Add all elements to the set (which doesn't allow duplicates), if the length of the set is the same as the original array then there are no dupes.
def containsDuplicate(nums: list[int]) -> bool:
    HashSet = set()
    
    for num in nums:
        HashSet.add(num)
    
    if len(HashSet) == len(nums):
        return False
    else:
        return True

print(containsDuplicate([1,2,3,1]))