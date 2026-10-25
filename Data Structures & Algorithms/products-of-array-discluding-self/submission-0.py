class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fw = [1] * n
        bw = [1] * n
        res = [0] * n
        curr = 1
        for i in range(1, n):
            curr *= nums[i-1]
            fw[i] = curr
        curr = 1
        for i in range(2, n+1):
            curr *= nums[-i+1]
            bw[-i] = curr
        for i in range(n):
            res[i] = fw[i]*bw[i]
        return res
        