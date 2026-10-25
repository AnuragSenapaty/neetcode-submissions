class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        alnum = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
        b = 0
        e = len(s)-1
        while b < e:
            while s[b] not in alnum and b<e:
                b+=1
            while s[e] not in alnum and b<e:
                e-=1
            print (s[b], s[e])
            print(alnum)
            if s[b].lower() != s[e].lower():
                return False
            b+=1
            e-=1
        return True

        