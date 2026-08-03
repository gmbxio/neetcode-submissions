class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subset = []
        def backtrack(idx: int, output: List[int]) -> None:
            if idx == len(nums):
                subset.append(output.copy())
                return 

            output.append(nums[idx])
            backtrack(idx + 1, output)
            output.pop()

            backtrack(idx + 1, output)

        backtrack(0, [])
        return subset
