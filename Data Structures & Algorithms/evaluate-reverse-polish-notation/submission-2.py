class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        digStack = []
        operators = ["+", "-", "*", "/"]

        for ch in tokens:
            if ch not in operators:
                digStack.append(int(ch))
            else:
                num2 = digStack.pop()
                num1 = digStack.pop()

                if ch == "+":
                    res = num1 + num2
                elif ch == "-":
                    res = num1 - num2
                elif ch == "*":
                    res = num1 * num2
                else:
                    res = int(num1 / num2)
                
                digStack.append(res)
        
        return digStack.pop()