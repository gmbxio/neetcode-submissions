class Solution:
    def medianIndex(self, arr: List[int], low: int, mid: int, high: int) -> int:
        if (arr[low] <= arr[mid] <= arr[high]) or (arr[low] >= arr[mid] >= arr[high]):
            return mid
        elif (arr[mid] >= arr[low] >= arr[high]) or (arr[mid] <= arr[low] <= arr[high]):
            return low
        else:
            return high


    def partition(self,arr: List[int], low: int, high: int) -> int:

        mid = (low + high)//2
        median_index = self.medianIndex(arr, low, mid, high)
        arr[median_index], arr[high] = arr[high], arr[median_index]
        pivot = arr[high]

        # partitioning
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[high], arr[i+1] = arr[i+1], arr[high] 
        return i+1

    def quickSort(self, nums: List[int], low: int, high: int) -> None:
            if low < high:
                pi = self.partition(nums, low, high)
                self.quickSort(nums, low, pi - 1)
                self.quickSort(nums, pi + 1, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums
        