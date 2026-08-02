class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesisList = []
        stack = []

        def generateComb(open: int, close: int, curr_str: str):

            if open == n and close == n:
                parenthesisList.append(curr_str)
                return 
            
            if open < n:
                generateComb(open + 1, close, curr_str + "(")

            if close < open:
                generateComb(open, close + 1, curr_str + ")")
            
        generateComb(0, 0, "")
        return parenthesisList