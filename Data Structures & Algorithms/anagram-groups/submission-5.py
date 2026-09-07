class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = defaultdict(list)

        for s in strs:
            frequency = Counter(s)
            r[frozenset(frequency.items())].append(s)

        return [val for val in r.values()]

        