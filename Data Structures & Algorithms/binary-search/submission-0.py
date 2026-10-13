class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b = 0
        e = len(nums) - 1
        while b <= e:
            mid = b + (e-b)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid - 1
            else:
                b = mid + 1
        return -1
        