class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in strs:
            sortedStr = "".join(sorted(i))
            if sortedStr not in anagram:
                anagram[sortedStr] = []
            anagram[sortedStr].append(i)
        
        rtn = []
        for i in anagram.values():
            rtn.append(i)
        
        return rtn

