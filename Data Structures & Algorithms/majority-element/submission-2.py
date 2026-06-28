class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityEle = 0
        count = 0
        for num in nums:
            if count == 0: majorityEle = num
            if num != majorityEle: count -= 1
            else: count += 1
        return majorityEle