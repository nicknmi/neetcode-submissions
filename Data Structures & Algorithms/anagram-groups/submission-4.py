class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rtn = defaultdict(list)

        for s in strs:
            frequency = Counter(s)
            rtn[frozenset(frequency.items())].append(s)

        return [val for val in rtn.values()]

        