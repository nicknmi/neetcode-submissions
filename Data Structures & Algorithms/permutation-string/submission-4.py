class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        frequency_s1 = [0] * 26
        frequency_substr = [0] * 26

        for char in s1:
            frequency_s1[ord(char) - ord('a')] += 1

        left = right = 0

        for _ in range(len(s1)):
            frequency_substr[ord(s2[right]) - ord('a')] += 1
            right += 1
            

        while right < len(s2):
            if frequency_substr == frequency_s1:
                return True

            frequency_substr[ord(s2[left]) - ord('a')] -= 1
            left += 1

            frequency_substr[ord(s2[right]) - ord('a')] += 1
            right += 1

        if frequency_substr == frequency_s1:
                return True

        return False

