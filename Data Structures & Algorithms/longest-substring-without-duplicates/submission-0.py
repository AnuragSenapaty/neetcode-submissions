class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        b = 0
        best = 0
        seen = set()
        for e in range(len(s)):
            while s[e] in seen:
                seen.remove(s[b])
                b += 1
            seen.add(s[e])
            best = max(best, e - b + 1)
        return best

        