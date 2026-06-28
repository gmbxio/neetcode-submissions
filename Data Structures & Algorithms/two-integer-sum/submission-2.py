class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, n in enumerate(nums):
            compliment =  target - n
            if compliment in mp:
                return [mp[compliment], i]
            mp[n] = i
        return []
    
    