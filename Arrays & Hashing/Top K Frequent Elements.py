# Done by creating a freqency table for the numbers in nums, then making an output table of length k. Iterate through the keys in the freqency table and 
# if the freqency is higher than the least frequent number in output, replace that number with this one.
def topKFrequent(nums: list[int], k: int) -> list[int]:
    HashMap = {}
    output = []
    
    for num in nums:
        if num in HashMap:
            HashMap[num] = HashMap[num] + 1
        else:
            HashMap[num] = 1
    
    def toBeReplaced(numsList, freqTable):
        currentLowest = (None, None)
        
        for ind, num in enumerate(numsList):
            if currentLowest == (None, None):
                currentLowest = (ind, freqTable[num])
            elif currentLowest[1] > freqTable[num]:
                currentLowest = (ind, freqTable[num])
            else:
                pass
            
        return currentLowest
    
    checkIfNeededToBeReplaced = True
    replaced = toBeReplaced(output, HashMap)
    
    for key, freq1 in HashMap.items():
        if len(output) < k:
            output.append(key)
        else:
            if checkIfNeededToBeReplaced:
                replaced = toBeReplaced(output, HashMap)
                checkIfNeededToBeReplaced = False
            
            if freq1 > replaced[1]:
                output[replaced[0]] = key
                checkIfNeededToBeReplaced = True
    
    return output

from collections import Counter

# Takes advantage of the Counter from collections having already implemented creating a freqency table and finding the k most common
def topKFrequentCounter(nums: list[int], k: int) -> list[int]:
    c = Counter(nums).most_common(k)
    output = []
    
    for x in c:
        output.append(x[0])
    return output
        
print(topKFrequent([5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3], 3))
print(topKFrequentCounter([5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3], 3))