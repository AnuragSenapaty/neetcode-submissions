from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Creates a list if a key does not exixt
        groups = defaultdict(list)

        for s in strs:
            #Sorted turns it into a list of chars, tuple makes it hashable,
            #so, anagarams should have the same tuple key.
            groups[tuple(sorted(s))].append(s)
        return list(groups.values())