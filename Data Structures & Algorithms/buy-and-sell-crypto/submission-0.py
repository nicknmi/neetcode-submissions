class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buy = 0
        sell = 1

        lowestPrice = prices[buy]
        highestPrice = prices[sell]

        maxProfit = highestPrice - lowestPrice


        while sell < len(prices):
            if prices[sell] < lowestPrice:
                buy = sell

                if buy == len(prices) - 1:
                    break

                sell += 1

                lowestPrice = prices[buy]
                highestPrice = prices[sell]

                continue


            if prices[sell] >= highestPrice:
                highestPrice = prices[sell]
                maxProfit = max(maxProfit, highestPrice - lowestPrice)

            sell += 1

        return max(maxProfit, 0)
