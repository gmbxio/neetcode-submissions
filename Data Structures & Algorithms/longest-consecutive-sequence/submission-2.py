class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        longlen = 0

        for num in nums:
            if num-1 not in numSet:
                currNum = num
                currlen = 1
            
                while currNum+1 in numSet:
                    currlen += 1
                    currNum += 1
                longlen = max(longlen, currlen)
        
        return longlen
