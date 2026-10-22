class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n > 1:
            max_prof = 0
            b = 0
            e = 1
            while e < n:
                prof = prices[e]-prices[b]
                max_prof = max(max_prof, prof)
                if prices[e] < prices[b]:
                    b = e
                    e += 1
                else:
                    e+=1
            return max_prof
        else:
            return 0
        