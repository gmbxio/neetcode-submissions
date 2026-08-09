class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sIdx = [0] * 26
        tIdx = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            sIdx[idx] += 1
        
        for ch in t:
            idx = ord(ch) - ord('a')
            tIdx[idx] += 1
        
        return sIdx == tIdx