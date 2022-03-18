class Bank {
  accounts: number[]
  constructor(balance: number[]) {
    this.accounts = balance
  }

  transfer(account1: number, account2: number, money: number): boolean {
    if (
      1 <= account1 &&
      account1 <= this.accounts.length &&
      1 <= account2 &&
      account2 <= this.accounts.length &&
      money <= this.accounts[account1 - 1]
    ) {
      this.accounts[account1 - 1] -= money
      this.accounts[account2 - 1] += money
      return true
    }
    return false
  }

  deposit(account: number, money: number): boolean {
    if (1 <= account && account <= this.accounts.length) {
      this.accounts[account - 1] += money
      return true
    }
    return false
  }

  withdraw(account: number, money: number): boolean {
    if (
      1 <= account &&
      account <= this.accounts.length &&
      money <= this.accounts[account - 1]
    ) {
      this.accounts[account - 1] -= money
      return true
    }
    return false
  }
}

/**
 * Your Bank object will be instantiated and called as such:
 * var obj = new Bank(balance)
 * var param_1 = obj.transfer(account1,account2,money)
 * var param_2 = obj.deposit(account,money)
 * var param_3 = obj.withdraw(account,money)
 */
