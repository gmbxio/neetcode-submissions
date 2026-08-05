class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = cost + [0]

        for i in range(n - 2, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])
