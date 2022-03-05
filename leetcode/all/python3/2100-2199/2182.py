class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        c = lambda x: ord(x) - ord('a')
        cc = lambda x: chr(ord('a') + x)
        cnt, ans = [0 for _ in range(26)], []
        for ch in s:
            cnt[c(ch)] += 1
        for i in range(25, -1, -1):
            k = i - 1
            while True:
                j = 0
                while j < repeatLimit and cnt[i] > 0:
                    ans.append(cc(i))
                    cnt[i] -= 1
                    j += 1
                if cnt[i] == 0:
                    break
                # 寻找间隔字母
                while k >= 0 and cnt[k] == 0:
                    k -= 1
                if k < 0:
                    break
                ans.append(cc(k))
                cnt[k] -= 1
        return ''.join(ans)
