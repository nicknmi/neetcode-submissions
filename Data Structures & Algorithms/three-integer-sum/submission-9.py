class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        # [-4, -1, 0, 1, 2]
        for i in range(len(nums) - 1):
            target = -nums[i]
            lower = i + 1
            upper = len(nums) - 1

            while lower < upper:
                sumPtrs = nums[lower] + nums[upper]

                if sumPtrs < target:
                    lower += 1
                elif sumPtrs > target:
                    upper -= 1
                else: 
                    a = [nums[i], nums[lower], nums[upper]]
                    lower += 1
                    upper -= 1
                    if a not in ans:
                        ans.append(a)



        return ans