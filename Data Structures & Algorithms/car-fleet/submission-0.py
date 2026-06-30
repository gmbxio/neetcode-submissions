class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carsSorted = sorted(zip(position, speed), reverse = True)

        time = []

        for p, s in carsSorted:
            timeTaken = (target - p)/s
            time.append(timeTaken)

            if len(time) >= 2 and time[-1] <= time[-2]:
                time.pop()
        
        return len(time)