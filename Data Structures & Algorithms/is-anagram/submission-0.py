class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFrequency = {}
        tFrequency = {}

        for l in s:
            sFrequency.setdefault(l, 0)
            sFrequency[l] += 1
        
        for l in t:
            tFrequency.setdefault(l, 0)
            tFrequency[l] += 1

        #print(sFrequency)
        #print(tFrequency)

        return sFrequency == tFrequency