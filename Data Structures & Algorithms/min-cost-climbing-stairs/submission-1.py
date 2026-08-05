class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first, second = cost[-1], 0 # dp[n -1] and dp[n]

        for i in range(n - 2, -1, -1):
            curr = cost[i] + min(first, second)
            second = first
            first = curr
        
        return min(first, second)
