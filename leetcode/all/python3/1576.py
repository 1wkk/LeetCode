class Solution:
    def modifyString(self, s: str) -> str:
        ans, n = [], len(s)

        if n == 1:
            return 'a' if s == '?' else s

        ch = ''
        for i in range(n):
            c = s[i]
            if c == '?':
                if 0 < i < n - 1:
                    lc = s[i - 1] if s[i - 1] != '?' else ch
                    rc = s[i + 1]
                    for i in range(ord('a'), ord('z') + 1):
                        ch = chr(i)
                        if ch != lc and ch != rc:
                            ans.append(ch)
                            break
                elif i == 0:
                    rc = s[i + 1]
                    for i in range(ord('a'), ord('z') + 1):
                        ch = chr(i)
                        if ch != rc:
                            ans.append(ch)
                            break
                elif i == n - 1:
                    lc = s[i - 1] if s[i - 1] != '?' else ch
                    for i in range(ord('a'), ord('z') + 1):
                        ch = chr(i)
                        if ch != lc:
                            ans.append(ch)
                            break
            else:
                ans.append(c)
        return ''.join(ans)
