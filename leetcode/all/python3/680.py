class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return valid(l + 1, r) or valid(l, r - 1)
            l, r = l + 1, r - 1
        return True
