class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracketMap = {")":"(", "]":"[", "}":"{"}

        for ch in s:
            if ch in bracketMap:
                stackTop = stack.pop() if stack else '69'
                if stackTop != bracketMap[ch]:
                    return False
            else:
                stack.append(ch)
        
        return not stack
