class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for (i, val) in enumerate(nums):
            remainder = target - val
            
            seen.setdefault(val, [])
            seen[val].append(i)   
            #print(seen)
            if (remainder) in seen and (seen[remainder][0] != i):
                return [seen[remainder].pop(0), i]

        return [0,0]

