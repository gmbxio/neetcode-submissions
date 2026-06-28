class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = defaultdict(list)
        for item in strs:
            itemSorted = tuple(sorted(item))
            group[itemSorted].append(item)
        groupAnagramList = list(group.values())
        return groupAnagramList