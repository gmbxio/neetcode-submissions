class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def findHours(k: int) -> int:
            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k
            
            return hours
        

        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2

            if findHours(mid) <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans