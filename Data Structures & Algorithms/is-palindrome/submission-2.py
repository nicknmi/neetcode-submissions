class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()

        lower = 0
        upper = len(s) - 1

        while (lower < upper):
            if not s[lower].isalnum():
                lower += 1
                continue
            if not s[upper].isalnum():
                upper -= 1
                continue
            
            if (s[lower].lower() != s[upper].lower()):
                return False
            
            lower += 1
            upper -= 1
        
        return True
            
            