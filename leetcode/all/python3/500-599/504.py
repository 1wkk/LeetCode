class Solution:
    def convertToBase7(self, number: int) -> str:
        if not number:
            return '0'
        ans = []
        flag, number = number > 0, abs(number)
        while number:
            ans.append(str(number % 7))
            number //= 7
        return ('' if flag else '-') + ''.join(ans[::-1])
