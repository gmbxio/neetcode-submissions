class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for n in nums:
            subset += [curr + [n] for curr in subset]
        return subset
