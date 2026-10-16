import bisect
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while(len(stones) > 1):
            heavy_1 = stones.pop()
            heavy_2 = stones.pop()
            heavy_1 -= heavy_2
            if heavy_1 > 0:
                bisect.insort(stones, heavy_1)
        if stones:
            return stones[0]
        return 0

        