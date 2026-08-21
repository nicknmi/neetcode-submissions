class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rt = defaultdict(list)

        for s in strs:
            frequency = Counter(s)
            rt[frozenset(frequency.items())].append(s)

        return [val for val in rt.values()]

        