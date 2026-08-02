class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        nums = sorted(nums)

        def solve(idx, output):
            if idx == len(nums):
                subset.append(output.copy())
                return 
            
            output.append(nums[idx])
            solve(idx + 1, output)
            output.pop()

            next_idx = idx + 1
            while next_idx < len(nums) and nums[next_idx] == nums[idx] :
                next_idx += 1        
                
            solve(next_idx, output)
        
        solve(0, [])
        return subset
