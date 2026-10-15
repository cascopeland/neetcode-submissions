class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # I think the idea here is to do this:
        # if l > r, set l = r, r = r + 1
        # then have a global_max = max(global, r- l)

        l=0
        r=1
        maxG = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                maxG = max(maxG, prices[r] - prices[l])
                r += 1
        return maxG