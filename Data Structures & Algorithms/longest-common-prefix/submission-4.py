class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for ch in zip(*strs):
            if len(set(ch)) == 1:
                prefix += ch[0]
            else:
                break
        return prefix
             
