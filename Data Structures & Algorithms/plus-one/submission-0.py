class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ret = []
        carry = 1
        for i in range(1, len(digits)+1):
            curr = int(digits[-i])
            curr += carry
            if curr > 9:
                ret.append("0")
                carry = 1
            else:
                ret.append(str(curr))
                carry = 0
        if carry:
            ret.append("1")
        ret.reverse()
        return ret

