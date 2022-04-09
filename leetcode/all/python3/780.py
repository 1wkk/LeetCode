class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx != ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if sx == tx and sy == ty:
            return True
        if sx == tx and sy < ty:
            return (ty - sy) % sx == 0
        if sx < tx and sy == ty:
            return (tx - sx) % sy == 0
        else:
            return False
