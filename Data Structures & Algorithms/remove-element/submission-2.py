class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lower = 0
        upper = len(nums) - 1
        k = 0

        while lower <= upper:            

            if nums[lower] == val:
                while nums[upper] == val and upper >= 0:
                    upper -= 1

                if upper < lower:
                    break
                    
                nums[lower] = nums[upper]
                nums[upper] = val


            k += 1
            lower += 1


        return k