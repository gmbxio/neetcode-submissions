class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []

        maxHeap = [(- nums[i], i) for i in range(k)]
        heapq.heapify(maxHeap)

        maxList = [-maxHeap[0][0]]

        for i in range(k, len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))

            while maxHeap[0][1] <= i-k:
                heapq.heappop(maxHeap)

            maxList.append(-maxHeap[0][0])
        
        return maxList
