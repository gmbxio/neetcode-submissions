class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] != val:
                left += 1
            elif nums[right] == val:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left