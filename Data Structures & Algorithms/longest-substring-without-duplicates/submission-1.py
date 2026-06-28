class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, longString = 0, 0
        length = len(s)
        seen = set()

        for right in range(length):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            else:
                seen.add(s[right])
                longString = max(longString, right - left + 1)
            
        return longString