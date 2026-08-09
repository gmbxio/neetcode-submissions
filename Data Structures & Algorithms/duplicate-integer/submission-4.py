class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCount = Counter(nums)

        for n in nums:
            if numCount[n] > 1:
                return True
        return False