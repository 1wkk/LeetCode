class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        dic = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ss = sentence.split(' ')
        for i, s in enumerate(ss):
            if s[0] in dic:
                s = s + 'ma'
            else:
                s = s[1:] + s[0] + 'ma'
            s = s + 'a' * (i + 1)
            ss[i] = s
        return ' '.join(ss)
