def twoSum(self, nums: List[int], target: int) -> List[int]:
    length = len(nums)

    for ind, num in enumerate(nums):
        # If we reach the last element, end the loop.
        if ind == length - 1:
            break

        # Iterate through the rest of the list to find a number that adds to target
        for i in range(ind + 1, length):
            if nums[i] + num == target:
                return [ind, i]