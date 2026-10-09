class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                t = t.replace(i, '', 1)
            else:
                return False
        if t == '':
            return True
        else:
            return False

        