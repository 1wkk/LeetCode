class Solution:
    def complexNumberMultiply(self, n_1: str, n_2: str) -> str:
        split_complex = lambda x: map(int, x.rstrip('i').split('+'))
        r_1, i_1 = split_complex(n_1)
        r_2, i_2 = split_complex(n_2)
        r_3 = r_1 * r_2 - i_1 * i_2
        i_3 = r_1 * i_2 + r_2 * i_1
        return '{}+{}i'.format(r_3, i_3)
