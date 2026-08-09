import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        heap = []

        for val, freq in count.items():
            heapq.heappush(heap, (freq, val))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for freq, val in heap:
            result.append(val)
        
        return result
        
          