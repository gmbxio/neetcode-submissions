class Solution:
    def medianIndex(self, arr: List[int], low: int, mid:int, high: int) -> int:
        if (arr[low] <= arr[mid] <= arr[high]) or (arr[low] >= arr[mid] >= arr[high]):
            return mid
        elif (arr[mid] <= arr[low] <= arr[high]) or (arr[mid] >= arr[low] >= arr[high]):
            return low
        else:
            return high


    def partition(self, arr: List[int], low: int, high: int) -> int:
        mid = (low + high) // 2
        median_index = self.medianIndex(arr, low, mid, high)
        # pivot
        pivot = arr[median_index]
        arr[median_index], arr[high] = arr[high], arr[median_index]

        # partioning
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1


    def quickSort(self, nums: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = self.partition(nums, low, high)
            self.quickSort(nums, low, partition_index-1)
            self.quickSort(nums, partition_index+1, high)

    def sortColors(self, nums: List[int]) -> None:
        self.quickSort(nums,0, len(nums) - 1)
        """
        Do not return anything, modify nums in-place instead.
        """
        