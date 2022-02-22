from collections import Counter, defaultdict
from math import gcd
from typing import List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        ct, MOD = Counter(nums), 10 ** 9 + 7
        dic = defaultdict(int)
        # 1 << ct[1] == 2 ** ct[1]
        # example: 1 1
        # [], [1], [1], [1, 1]
        # [] is valid, because [] + [2] = [2] is valid
        dic[1] = (1 << ct[1]) % MOD
        # 这些数均不包含平方因子
        for n in [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]:
            # dic size changes during iteration
            for x in list(dic):
                if gcd(n, x) == 1:
                    dic[n * x] = (dic[n * x] + dic[x] * ct[n]) % MOD
        return (sum(dic.values()) - dic[1]) % MOD
