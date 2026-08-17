class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rt = defaultdict(list)

        for str_ in strs:
            frequency = Counter(str_)
            rt[frozenset(frequency.items())].append(str_)

        return [val for val in rt.values()]

        