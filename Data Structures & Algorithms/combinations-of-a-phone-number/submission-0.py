class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        map = {"2": "abc",
               "3": "def",
               "4": "ghi",
               "5": "jkl",
               "6": "mno",
               "7": "pqrs",
               "8": "tuv",
               "9": "wxyz"}
        
        ans = []

        def backtrack(idx: int, currSt: str) -> None:
            if len(currSt) == len(digits):
                ans.append(currSt)
                return 
            
            for ch in map[digits[idx]]:
                backtrack(idx + 1, currSt + ch)
        
        backtrack(0, "")
        return ans