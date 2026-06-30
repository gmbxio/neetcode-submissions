class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempstack = []
        dayslist = [0]*(len(temperatures))

        for i, temp in enumerate(temperatures):

            while tempstack and temp > temperatures[tempstack[-1]]:
                previndex = tempstack.pop()
                dayslist[previndex] = i - previndex
            
            tempstack.append(i)
        
        return dayslist
