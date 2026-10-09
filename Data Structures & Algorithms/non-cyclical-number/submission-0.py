class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        while True:
            happy = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                happy += digit * digit

            if happy == 1:
                return True
            if happy == 4:
                return False
            n = happy