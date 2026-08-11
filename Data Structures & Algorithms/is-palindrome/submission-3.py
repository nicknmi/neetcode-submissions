class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        lower = 0
        upper = len(s) - 1

        while (lower < upper):
            while lower < upper and not s[lower].isalnum():
                lower += 1
            while upper > lower and not s[upper].isalnum():
                upper -= 1
            
            if (s[lower] != s[upper]):
                return False
            
            lower += 1
            upper -= 1
        
        return True
            
            