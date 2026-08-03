class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = nums

        def solve(idx: int) -> None:
            if idx == len(nums):
                result.append(temp.copy())
                return
            
            for i in range(idx, len(nums)):

                temp[idx], temp[i] = temp[i], temp[idx]
                solve(idx + 1)
                temp[idx], temp[i] = temp[i], temp[idx]
        
        solve(0)
        return result
            

            