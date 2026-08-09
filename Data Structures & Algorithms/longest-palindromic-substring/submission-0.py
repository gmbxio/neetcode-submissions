class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longPal = ""

        def expandFromCentre(l: int, r: int) -> str:

            while l >= 0 and r < n:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break 
            return s[l + 1:r]

        
        for i in range(n):
            oddsub = expandFromCentre(i, i)
            evensub = expandFromCentre(i, i + 1)

            if len(oddsub) > len(longPal):
                longPal = oddsub
            if len(evensub) > len(longPal):
                longPal = evensub

        return longPal