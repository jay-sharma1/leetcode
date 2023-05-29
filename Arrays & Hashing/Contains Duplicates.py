def containsDuplicate(nums: List[int]) -> bool:
    final_set = set()
    for i in nums:
        final_set.add(i)

    if len(final_set) < len(nums):
        return True
    else:
        return False
