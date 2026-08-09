class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = defaultdict(list)

        for str in strs:
            idxmap = [0] * 26
            for ch in str:
                idx = ord(ch) - ord('a')
                idxmap[idx] += 1
            group[tuple(idxmap)].append(str)

        return list(group.values())



            