def containsDuplicate(nums: List[int]) -> bool:
    final_set = set()

    # Initialize and add all numbers in nums to the set.
    for i in nums:
        final_set.add(i)

    # If the length of the set is smaller than of the original list, there must be duplicates.
    if len(final_set) < len(nums):
        return True
    else:
        return False
