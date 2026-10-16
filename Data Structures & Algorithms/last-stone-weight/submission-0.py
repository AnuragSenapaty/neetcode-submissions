class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) > 1):
            stones.sort()
            heavy_1 = stones.pop()
            heavy_2 = stones.pop()

            heavy_1 -= heavy_2
            if heavy_1 > 0:
                stones.append(heavy_1)
        if stones:
            return stones[0]
        return 0

        