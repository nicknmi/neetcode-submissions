class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lower = 0
        upper = len(numbers) - 1
        while lower < upper:
            two_sum = numbers[lower] + numbers[upper]
            if two_sum > target:
                upper -= 1
            elif two_sum < target:
                lower += 1
            else:
                break
        return [lower + 1, upper + 1]
