class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, maxlen = 0, 0
        lastseen = {}

        for right in range(len(s)):
            
            if s[right] in lastseen and lastseen[s[right]] >= left:
                left = lastseen[s[right]] + 1

            lastseen[s[right]] = right
            maxlen = max(maxlen, right - left + 1)
            
        return maxlen