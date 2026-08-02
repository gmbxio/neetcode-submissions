class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates = sorted(candidates)

        def solve(idx: int, currTarget: int, path : List[int]) -> None:
            if currTarget == 0:
                result.append(path.copy())
                return 

            if idx == len(candidates) or currTarget < 0:
                return

            if candidates[idx] <= target:
                path.append(candidates[idx])
                solve(idx + 1, currTarget - candidates[idx], path)
                path.pop()

            next_idx = idx + 1
            while next_idx < len(candidates) and candidates[next_idx] == candidates[idx]:
                next_idx += 1

            solve(next_idx, currTarget, path)
        
        solve(0, target, [])
        return result