class Solution:
    def lengthLongestPath(self, input: str) -> int:
        ans = 0
        dep = {-1: 0}
        for s in input.split('\n'):
            c = s.count('\t')
            # `-c` 是因为 `\t` 只算一个字符，TS 中也一样
            dep[c] = dep[c - 1] + len(s) - c
            if s.__contains__('.'):
                ans = max(ans, dep[c] + c)
        return ans
