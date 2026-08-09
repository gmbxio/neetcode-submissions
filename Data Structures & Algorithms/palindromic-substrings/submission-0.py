class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expandFromCentre(l: int, r: int) -> None:
            nonlocal count
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break
        
        for i in range(n):
            oddsub = expandFromCentre(i, i)
            evensub = expandFromCentre(i, i + 1)

        return count