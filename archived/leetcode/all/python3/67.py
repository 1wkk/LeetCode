class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, carry = '', 0
        for i in range(max(len(a), len(b))):
            carry += int(a[-(i + 1)]) if i < len(a) else 0
            carry += int(b[-(i + 1)]) if i < len(b) else 0
            ans += str(carry % 2)
            carry //= 2
        if carry > 0:
            ans += str(carry)
        return ans[::-1]
