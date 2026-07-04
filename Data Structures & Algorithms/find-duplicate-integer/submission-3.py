class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            val = abs(nums[i])
            if nums[val - 1] < 0:
                return val
            nums[val - 1] *= -1