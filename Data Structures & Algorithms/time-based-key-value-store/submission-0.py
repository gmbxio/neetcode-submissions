class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.map.get(key, [])
        val = ""

        left, right = 0, len(vals) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if vals[mid][0] <= timestamp:
                val = vals[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return val
