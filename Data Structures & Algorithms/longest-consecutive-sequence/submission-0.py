class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)
        runningLongest = 0
        
        for num in nums:
            # check if start of sequence
            if num - 1 in set_:
                continue

            longest = 0
            num2 = num
            while num2 + 1 in set_:
                num2 += 1
                longest += 1
            
            runningLongest = max(runningLongest, longest + 1)
        
        return runningLongest

        



            

