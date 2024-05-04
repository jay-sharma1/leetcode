# Iterate through the list and for each string, sort it. The sorted string is now a key in the dict. If the result of sorting a string is already a key, add it to the value array
# for that string. In the end you will have a set of sorted keys, whose values are a list of every original word that when sorted produces that key.
def groupAnagrams(strs):
    HashMap = {}
    
    for word in strs:
        sort = ''.join(sorted(word))
        
        if sort in HashMap:
            HashMap[sort].append(word)
        else:
            HashMap[sort] = [word]
    
    output = []
    
    for value in HashMap.values():
        output.append(value)
    
    return output
    

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))