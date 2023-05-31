def isAnagram(self, s: str, t: str) -> bool:
    # If string lengths are unequal, they cannot be anagrams
    if len(s) != len(t):
        return False

    freq_table1 = {}
    freq_table2 = {}

    # Add each character of both strings to separate dictionaries
    for ind in range(len(s)):
        char1 = s[ind]
        char2 = t[ind]
        in_table1 = freq_table1.get(char1)
        in_table2 = freq_table2.get(char2)

        if in_table1 is None:
            freq_table1.update({char1: 1})
        else:
            freq_table1.update({char1: in_table1 + 1})

        if in_table2 is None:
            freq_table2.update({char2: 1})
        else:
            freq_table2.update({char2: in_table2 + 1})

    # Equivalent dictionaries mean both strings must be anagrams
    if freq_table1 == freq_table2:
        return True
    else:
        return False
