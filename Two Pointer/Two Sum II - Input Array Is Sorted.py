def twoSum(numbers: list[int], target: int) -> list[int]:
    leftPointer = 0
    rightPointer = len(numbers) - 1
    
    while leftPointer < rightPointer:
        total = numbers[leftPointer] + numbers[rightPointer]
        
        if total == target:
            return [leftPointer + 1, rightPointer + 1]
        elif total > target:
            rightPointer -= 1
        else:
            leftPointer += 1

#Test
print(twoSum([2,7,11,15], 9))