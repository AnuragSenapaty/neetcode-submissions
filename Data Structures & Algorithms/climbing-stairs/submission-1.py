class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        a = 1
        b = 2
        flag = True
        for i in range(n-2):
            if flag:
                a = a + b
                flag = not flag
            else:
                b = a + b
                flag = not flag
        if flag:
            return b
        else:
            return a