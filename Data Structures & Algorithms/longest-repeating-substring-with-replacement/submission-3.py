class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        left = 0
        longest = 0
        frequencies = {}
        max_freq = 0
        
        for right in range(len(s)):
            frequencies[s[right]] = frequencies.get(s[right], 0) + 1
            max_freq = max(max_freq, frequencies[s[right]])

            while (right - left + 1) - max_freq > k:
                frequencies[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left+1)
        return longest