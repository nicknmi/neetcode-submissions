class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        sFrequency = {}
        tFrequency = {}

        for i in range(len(s)):
            sFrequency.setdefault(s[i], 0)
            sFrequency[s[i]] += 1
            tFrequency.setdefault(t[i], 0)
            tFrequency[t[i]] += 1

        #print(sFrequency)
        #print(tFrequency)

        return sFrequency == tFrequency