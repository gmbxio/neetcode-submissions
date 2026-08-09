class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
            
        rob1, rob2 = 0, 0

        for i in range(n - 1):
            robVal = max((nums[i] + rob1), rob2)
            rob1 = rob2
            rob2 = robVal
        
        firstRob = rob2 

        rob1, rob2 = 0, 0
        for i in range(1, n):
            robVal = max((nums[i] + rob1), rob2)
            rob1 = rob2
            rob2 = robVal

        lastRob = rob2

        return max(firstRob, lastRob)
        
