class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowerRate = 1
        upperRate = max(piles)

        midRate = (upperRate + lowerRate) // 2
        
        minK = upperRate

        while lowerRate <= midRate:
            hours = 0

            # calculate hours needed to eat all bananas
            # given the current eating rate
            for pile in piles:
                hours += pile // midRate

                if pile % midRate != 0:
                    hours += 1

            if hours <= h:
                minK = min(minK, midRate)

            if hours > h:
                lowerRate = midRate + 1
            else:
                upperRate = midRate - 1

            midRate = (upperRate + lowerRate) // 2


        return minK