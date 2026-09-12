class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):            
            for _str in strs:
                if i == len(_str) or _str[i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]

        