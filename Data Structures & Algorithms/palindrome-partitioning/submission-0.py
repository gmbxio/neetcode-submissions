class Solution:
    def partition(self, s: str) -> List[List[str]]:
        substr = []
        comb = []

        def isPalindrome(s: str) -> bool:
            l, r = 0, len(s) - 1
            
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1

                else:
                    return False
            
            return True 


        def backtrack(idx: int) -> None:
            if idx == len(s):
                substr.append(comb.copy())
                return 
            
            for end in range(idx + 1, len(s) + 1):
                subs = s[idx: end]
                if isPalindrome(subs):
                    comb.append(subs)
                    backtrack(end)
                    comb.pop()
                
        backtrack(0)
        return substr
