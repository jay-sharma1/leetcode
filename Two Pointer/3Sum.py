def threeSum(nums: list[int]) -> list[list[int]]:
        pass
    
def twoSum(nums: list[int], firstIndex: int) -> list[int]:
    # Target is 0 - i, so we only need to find j and k that add up to the target, such that
    # j + k == 0 - i  -> i + j + k == 0
    target = 0 - nums[firstIndex]
    
    