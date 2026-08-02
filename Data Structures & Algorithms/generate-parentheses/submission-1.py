class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesisList = []

        def generateComb(open: int, close: int, stack: List[str]):

            if open == n and close == n:
                parenthesisList.append("".join(stack))
                return 
            
            if open < n:
                stack.append("(")
                generateComb(open + 1, close, stack)
                stack.pop()

            if close < open:
                stack.append(")")
                generateComb(open, close + 1, stack)
                stack.pop()
            
        generateComb(0, 0, [])
        return parenthesisList