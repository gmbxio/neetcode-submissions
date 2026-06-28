class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longCommonPrefix = ""
        strs.sort()
        strs_first = strs[0]
        strs_last = strs[len(strs)-1]
        m = min(len(strs_first), len(strs_last))
        for i in range(m):
            if strs_first[i] != strs_last[i]:
                break
            else:
                longCommonPrefix += strs_first[i]
        return longCommonPrefix
        
             
