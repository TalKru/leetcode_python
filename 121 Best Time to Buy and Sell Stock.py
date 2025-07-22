"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day
to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed
because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Even though the two if statements are independent,
        their ordering in the code is what matters:
        1. Compute profit using yesterday’s best price.
        2. Then possibly update the best price for tomorrow.
        """
        best_price: int = prices[0]
        max_profit: int = 0

        for i in range(1, len(prices)):
            profit = prices[i] - best_price  # profit if sold today

            # can selling today beat our best profit?
            # always compute the potential profit before you ever change best_price
            if profit > max_profit:
                max_profit = profit

            # can we buy today for cheaper?
            if prices[i] < best_price:
                best_price = prices[i]

        return max_profit


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [1, 2, 3, 4, 5],
        [2, 4, 1],
        [5],
        [3, 3, 3, 3],
        [20, 50, 20, 3, 1, 2],
    ]

    for prices in test_cases:
        result = sol.maxProfit(prices)
        print(f"prices = {prices} -> maxProfit = {result}")

