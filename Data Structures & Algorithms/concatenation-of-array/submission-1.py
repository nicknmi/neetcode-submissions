class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)

        arrLen = len(nums)

        for i, num in enumerate(nums):
            ans[i] = num
            ans[i+arrLen] = num

        return ans