class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for h in range(len(heights)):
            popped = (h, heights[h])
            while stack and heights[h] < stack[-1][1]:
                maxArea = max(maxArea, (h - stack[-1][0])*stack[-1][1])
                popped = stack.pop()
            stack.append((popped[0], heights[h]))
        
        while stack:
            popped = stack.pop()
            maxArea = max(maxArea, (len(heights)-popped[0])*popped[1])
        return maxArea