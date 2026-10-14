class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[2]+nums[0], nums[1])
        
        tot = [0] * n
        tot[0] = nums[0]
        tot[1] = nums[1]
        tot[2] = max(nums[2]+tot[0], tot[1])
        for i in range(3, n):
            tot[i] = max(tot[i-3] + nums[i], tot[i-2] + nums[i], tot[i-1])
        return tot[n-1]
        
