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
