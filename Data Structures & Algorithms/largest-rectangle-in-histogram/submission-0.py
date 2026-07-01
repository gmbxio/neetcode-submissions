class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights.append(0)
        stack = [-1]
        largeRect = 0

        for ind, height in enumerate(heights):
            while stack[-1] != -1 and height < heights[stack[-1]]:

                h = heights[stack.pop()]
                w = ind - stack[-1] - 1

                largeRect = max(largeRect, h*w)
            
            stack.append(ind)
        
        heights.pop()
        return largeRect 