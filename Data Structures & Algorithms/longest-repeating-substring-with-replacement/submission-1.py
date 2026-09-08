class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        
        frequency = defaultdict(int)
        mostfrqchar = (s[0], 1)

        left = 0
        right = 0
        maxLen = 1

        while right < len(s):
            frequency[s[right]] += 1
            mostfrqchar = max(frequency.items(), key=lambda item: item[1])

            distinctfrq = sum(frequency.values()) - mostfrqchar[1]

            if distinctfrq > k:
                while distinctfrq > k:
                    frequency[s[left]] -= 1

                    mostfrqchar = max(frequency.items(), key=lambda item: item[1])
                    distinctfrq = sum(frequency.values()) - mostfrqchar[1]

                    left += 1

            maxLen = max(maxLen, right-left+1)

            right += 1
        
    
        return maxLen   


