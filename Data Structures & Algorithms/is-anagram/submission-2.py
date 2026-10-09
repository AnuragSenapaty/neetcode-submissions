class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_let = {}
        for i in s:
            if i in s_let:
                s_let[i] += 1
            else:
                s_let[i] = 1
        for i in t:
            if i in s_let:
                s_let[i] -= 1
            else:
                return False
        for i in s_let:
            if s_let[i] != 0:
                return False
        return True
                