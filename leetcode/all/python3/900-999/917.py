class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ss, l, r = list(s), 0, len(s) - 1
        while l < r:
            while l < r and not ss[l].isalpha():
                l += 1
            while l < r and not ss[r].isalpha():
                r -= 1
            if l < r:
                ss[l], ss[r] = ss[r], ss[l]
                l, r = l + 1, r - 1
        return ''.join(ss)
