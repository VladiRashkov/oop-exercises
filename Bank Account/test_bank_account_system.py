import unittest
from bank_account_system import BankAccount, SavingsAccount 

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(1000, 'Gary', '12415151')

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw(self):
        self.account.withdraw(500)
        self.assertEqual(self.account.balance, 500)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1500)

    def test_withdraw_negative(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

    def test_balance(self):
        self.assertEqual(self.account.balance, 1000)


class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        self.savings = SavingsAccount(2000, 'Ryan', '124151', 0.1)

    def test_one_year_interest(self):
        self.savings.one_year_interest()
        self.assertEqual(self.savings.balance, 2200)

    def test_negative_balance_interest(self):
        self.savings._balance = -100
        with self.assertRaises(ValueError):
            self.savings.one_year_interest()

    def test_balance(self):
        self.assertEqual(self.savings.balance, 2000)


if __name__ == '__main__':
    unittest.main()
