class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        highestLeft = height[left]

        right = len(height) - 1
        highestRight = height[right]

        sumWater = 0

        while left < right:
            if highestLeft > highestRight:
                right -= 1

                highestRight = max(highestRight, height[right])
                sumWater += highestRight - height[right]
            
            else:
                left += 1

                highestLeft = max(highestLeft, height[left])
                sumWater += highestLeft - height[left]

            


        return sumWater 

        
