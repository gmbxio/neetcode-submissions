class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num,0)+1
        for key, count in frequency_map.items():
            if count > n / 2:
                return key