import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0)+1
        
        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            
        while len(heap) > k:
            heapq.heappop(heap)

        result = []
        for freq, num in heap:
            result.append(num)

        return result