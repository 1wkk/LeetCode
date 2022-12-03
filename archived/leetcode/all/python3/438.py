from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p, ans = len(s), len(p), []
        if len_p > len_s:
            return ans
        ct_s, ct_p = [0 for _ in range(26)], [0 for _ in range(26)]
        for i in range(len_p):
            ct_s[ord(s[i]) - ord('a')] += 1
            ct_p[ord(p[i]) - ord('a')] += 1
        if ct_s == ct_p:
            ans.append(0)
        for i in range(len_p, len_s):
            ct_s[ord(s[i]) - ord('a')] += 1
            ct_s[ord(s[i - len_p]) - ord('a')] -= 1
            if ct_s == ct_p:
                ans.append(i - len_p + 1)
        return ans
