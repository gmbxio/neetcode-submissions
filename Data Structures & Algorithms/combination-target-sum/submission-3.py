class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
    
        def solve(idx: int, currTarget: int, path : List[int]) -> None:
            if currTarget == 0:
                result.append(path.copy())
                return 

            if idx == len(nums) or currTarget < 0:
                return

            path.append(nums[idx])
            solve(idx, currTarget - nums[idx], path)
            path.pop()

            solve(idx + 1, currTarget, path)
        
        solve(0, target, [])
        return result