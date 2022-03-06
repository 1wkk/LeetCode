#
# @lc app=leetcode.cn id=2034 lang=python3
#
# [2034] 股票价格波动
#

# @lc code=start


from sortedcontainers import SortedList


class StockPrice:
    def __init__(self):
        self.sl = SortedList()
        self.dic = dict()
        self.cur = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.dic:
            self.sl.remove(self.dic[timestamp])
        self.dic[timestamp] = price
        self.sl.add(price)
        self.cur = max(self.cur, timestamp)

    def current(self) -> int:
        return self.dic[self.cur]

    def maximum(self) -> int:
        return self.sl[-1]

    def minimum(self) -> int:
        return self.sl[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
# @lc code=end
