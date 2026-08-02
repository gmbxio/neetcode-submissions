class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesisList = []
        stack = []

        def generateComb(open: int, close: int):

            if open == n and close == n:
                parenthesisList.append("".join(stack))
                return 
            
            if open < n:
                stack.append("(")
                generateComb(open + 1, close)
                stack.pop()

            if close < open:
                stack.append(")")
                generateComb(open, close + 1)
                stack.pop()
            
        generateComb(0, 0)
        return parenthesisList