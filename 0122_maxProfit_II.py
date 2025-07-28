class Solution:
    def maxProfit(self, prices):
        # maxP = 0
        # startP = prices[0]
        # len1 = len(prices)
        # for i in range(1, len1):
        #     if startP < prices[i]:
        #         maxP += prices[i] - startP
        #     startP = prices[i]
        # return maxP

        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit += prices[r] - prices[l]
            l = r
            r += 1
        return profit

    # O(n),O(1)

if __name__ == '__main__':
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(sol.maxProfit(prices))