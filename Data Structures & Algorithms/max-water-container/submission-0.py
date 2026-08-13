class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0
        lower = 0
        upper = len(heights) - 1
        
        while lower < upper:
            lowerHeight = heights[lower]
            upperHeight = heights[upper]

            lowestHeight = min(lowerHeight, upperHeight)
            area = lowestHeight * (upper - lower)

            largestArea = max(largestArea, area)

            if lowerHeight < upperHeight:
                lower += 1
            elif upperHeight < lowerHeight:
                upper -= 1
            else:
                lower += 1
                upper -= 1
        
        return largestArea
