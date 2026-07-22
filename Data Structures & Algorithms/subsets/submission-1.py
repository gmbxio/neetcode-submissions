class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []

        def solve(ip: List[int], op: List[int]) -> None:
            if not ip:
                subset.append(op)
                return
            
            solve(ip[1: ], op)
            solve(ip[1: ], op + [ip[0]])

        solve(nums, [])
        return subset
