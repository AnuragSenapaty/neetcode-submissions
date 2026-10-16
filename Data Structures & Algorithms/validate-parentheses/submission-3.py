class Solution:
    def isValid(self, s: str) -> bool:
        curr = []
        for i in s:
            if i in "({[":
                curr.append(i)
            else:
                try:
                    rem = curr.pop()
                except:
                    return False
                if i == ']' and rem != '[':
                    return False
                elif i == ')' and rem != '(':
                    return False
                elif i == '}' and rem != '{':
                    return False
        if curr:
            return False
        return True
        