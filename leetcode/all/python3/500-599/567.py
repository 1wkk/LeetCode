class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        ct1, ct2 = [0 for _ in range(26)], [0 for _ in range(26)]
        for i in range(len1):
            ct1[ord(s1[i]) - ord('a')] += 1
            ct2[ord(s2[i]) - ord('a')] += 1
        if ct1 == ct2:
            return True
        for i in range(len1, len2):
            ct2[ord(s2[i]) - ord('a')] += 1
            ct2[ord(s2[i - len1]) - ord('a')] -= 1
            if ct1 == ct2:
                return True
        return False
