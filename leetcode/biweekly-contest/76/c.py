from typing import List


class ATM:
    def __init__(self):
        self.db = [0] * 5
        self.prices = [500, 200, 100, 50, 20]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.db[i] += banknotesCount[4 - i]

    def withdraw(self, amount: int) -> List[int]:
        db = self.db.copy()
        pay = [0] * 5
        for i in range(5):
            if db[i] < 1:
                continue
            if self.prices[i] <= amount:
                pay[4 - i] = min(amount // self.prices[i], db[i])
                amount -= pay[4 - i] * self.prices[i]
                db[i] -= pay[4 - i]
        if amount > 0:
            return [-1]
        else:
            self.db = db
            return pay


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
