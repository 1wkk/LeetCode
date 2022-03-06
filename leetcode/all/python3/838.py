class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        lt = list(dominoes)
        _len, l, ll = len(lt), 0, 'L'
        while l < _len:
            if lt[l] == '.':
                r = l
                # find closet forge
                while r < _len and lt[r] == '.':
                    r += 1
                rr = lt[r] if r < _len else 'R'
                # change
                if ll == rr:
                    while l < r:
                        lt[l] = ll
                        l += 1
                elif ll == 'R' and rr == 'L':
                    k = r - 1
                    while l < k:
                        lt[l] = 'R'
                        lt[k] = 'L'
                        l, k = l + 1, k - 1
                # next turn
                ll = rr
                l = r + 1
            else:
                ll = lt[l]
                l += 1
        return ''.join(lt)
