class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        # first pass: get all letter frequencies
        for i in strs:
            frequency = self.freeze(Counter(i))
            if (frequency not in anagrams):
                anagrams[frequency] = []
            anagrams[frequency].append(i)

        rtn = []
        for i in anagrams.values():
            rtn.append(i)
            
        return rtn

    def freeze(self, counter):
        return frozenset(counter.items())
