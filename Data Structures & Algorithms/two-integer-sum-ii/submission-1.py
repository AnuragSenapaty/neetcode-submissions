class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        b, e = 0, len(numbers)-1
        while b < e:
            cur = numbers[b] + numbers[e]
            if cur == target:
                return [b+1, e+1]
            elif cur > target:
                e-=1
            else:
                b+=1
        