from collections import Counter

# Simply add each character of both strings to their own frequency tables. If the frequency tables are identical, then they are anagrams.
# In this case the code is simplified by using a Counter, which takes a string input and creates a dict of each of its characters and their frequencies

def isAnagram(self, s: str, t: str) -> bool:
    # If string lengths are unequal, they cannot be anagrams
    if len(s) != len(t):
        return False

    freqTable1 = Counter(s)
    freqTable2 = Counter(t)
    
    if freqTable1 == freqTable2:
        return True
    else:
        return False
    
