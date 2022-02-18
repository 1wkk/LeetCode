#
# @lc app=leetcode.cn id=2047 lang=python3
#
# [2047] 句子中的有效单词数
#

# @lc code=start
class Solution:
    def countValidWords(self, sentence: str) -> int:
        ss = sentence.split()
        ans = 0
        for s in ss:
            flag = True
            hyphen = 0
            for i in range(len(s)):
                c = s[i]
                if str.isdigit(c):
                    flag = False
                    break
                elif c in ["!", ".", ","]:
                    if i != len(s) - 1:
                        flag = False
                elif c == "-":
                    hyphen += 1
                    if (
                        hyphen > 1
                        or i == 0
                        or i == len(s) - 1
                        or (not str.isalpha(s[i - 1]) or not str.isalpha(s[i + 1]))
                    ):
                        flag = False
                        break
            if flag:
                ans += 1
        return ans


# @lc code=end
