class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list2 = nums
        list2.extend(nums)
        return list2
