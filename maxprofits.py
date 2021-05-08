# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
from math import max

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxCurr = 0
        maxSoFar = 0
        
        for i in range (1, len(prices)+1):
            maxCurr = max(0, maxCurr += prices[i] - prices[i-1])
        `
            
                for(int i = 1; i < prices.length; i++) {
            maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);
            maxSoFar = Math.max(maxCur, maxSoFar);
        }
        return maxSoFar;
    }
