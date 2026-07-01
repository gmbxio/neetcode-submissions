class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        ans = nums[low]

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[high]:
                ans = min(ans, nums[high])
                low = mid + 1
            else:
                ans = min(ans,nums[mid])
                high = mid - 1

        return ans