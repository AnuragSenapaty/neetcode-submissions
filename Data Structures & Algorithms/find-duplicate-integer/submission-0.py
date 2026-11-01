class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_u = set()
        for i in nums:
            if i in nums_u:
                return i
            else:
                nums_u.add(i)
        