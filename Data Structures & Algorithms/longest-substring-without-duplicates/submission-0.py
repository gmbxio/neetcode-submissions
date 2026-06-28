class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, longString = 0, 0, 0
        length = len(s)
        seen = set()

        while right < length:

            if s[right] in seen:
                seen.remove(s[left])
                left += 1

            else:
                seen.add(s[right])
                longString = max(longString, right - left + 1)
                right += 1
            
        return longString