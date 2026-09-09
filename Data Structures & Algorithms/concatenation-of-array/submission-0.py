class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)

        arrLen = len(nums)

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+arrLen] = nums[i]

        return ans