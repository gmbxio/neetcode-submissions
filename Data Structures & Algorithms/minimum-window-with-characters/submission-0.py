class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        charFreq = Counter(t)

        left, right = 0, 0
        minLen, count, startInd = 10000, 0, -1

        while right < len(s):
            if charFreq[s[right]] > 0:
                count += 1
            charFreq[s[right]] -= 1
            
            while count == len(t):
                currWinLen = right - left + 1
                if currWinLen < minLen:
                    minLen = currWinLen
                    startInd = left

                charFreq[s[left]] += 1

                if charFreq[s[left]] > 0:
                    count -= 1
                left += 1
            right += 1
        
        if minLen == 10000:
            return ""
        else:
            return s[startInd: startInd+minLen]
