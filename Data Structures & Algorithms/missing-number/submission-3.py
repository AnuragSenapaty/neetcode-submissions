class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[0]
        for i in range(len(nums)):
            if nums[i] != n+i:
                return n+i
        if nums[0] != 0:
            return 0
        else:
            return n+i+1


        