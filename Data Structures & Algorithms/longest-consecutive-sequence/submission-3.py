class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numset = set(nums)
        longlen = 1

        for num in nums:
            if num - 1 not in numset:
                startnum = num
                currlen = 1

                while startnum + 1 in numset:
                    currlen += 1
                    startnum += 1
                
                longlen = max(longlen, currlen)
        
        return longlen 


