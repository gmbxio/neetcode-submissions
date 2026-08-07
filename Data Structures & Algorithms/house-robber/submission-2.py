class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            nextRob = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = nextRob
             
        return rob2