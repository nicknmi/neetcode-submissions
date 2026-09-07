class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        maxLen = 1
        left = right = 0
        
        seen = set()

        while right < len(s):
            if s[right] in seen:
                while left < right and s[right] in seen:
                    seen.remove(s[left])
                    left += 1

            seen.add(s[right])

            maxLen = max(maxLen, len(seen))
            right += 1


        return maxLen


