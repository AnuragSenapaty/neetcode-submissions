class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums:
            cont = set()
            for i in nums:
                if i in cont:
                    return True
                else:
                    cont.add(i)
            return False
        else:
            return False
        