class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = nums

        def solve(idx: int, comb: List[int]) -> None:
            if idx == len(comb):
                result.append(comb.copy())
                return
            
            for i in range(idx, len(nums)):

                comb[idx], comb[i] = comb[i], comb[idx]
                solve(idx + 1, comb)
                comb[idx], comb[i] = comb[i], comb[idx]
        
        solve(0, temp)
        return result
            

            