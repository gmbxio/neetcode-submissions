class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,longString = 0, 0
        chFreq = {}
        maxFreq = 0

        for right in range(len(s)):
            chFreq[s[right]] = chFreq.get(s[right], 0)+1

            maxFreq = max(maxFreq, chFreq[s[right]])
            winSize = (right - left + 1)

            replace = winSize - maxFreq

            if replace > k:
                chFreq[s[left]] -= 1
                left += 1
            
            else:
                longString = max(longString, right - left + 1)
        
        return longString


