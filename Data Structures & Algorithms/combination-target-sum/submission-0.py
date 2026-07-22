class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        path = []
    

        def solve(idx: int, currTarget: int) -> None:
            if idx == len(nums) or currTarget < 0:
                return
            if currTarget == 0:
                result.append(path.copy())
                return 

            path.append(nums[idx])
            solve(idx, currTarget - nums[idx])

            path.pop()
            solve(idx + 1, currTarget)
        
        solve(0, target)
        return result