class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequencyS = defaultdict(int)
        frequencyT = defaultdict(int)

        for char in s:
            frequencyS[char] += 1
        
        for char in t:
            frequencyT[char] += 1

        
        return frequencyT == frequencyS
