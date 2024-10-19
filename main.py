from bank import SavingsAccount, CurrentAccount

john = SavingsAccount(9030866377, "Savings", 5000, "Johnson")
sam = CurrentAccount(654289, "Current", 10000, "Samuel")

print(john.get_account_details())

print(john.deposit(500))
print(john.withdraw(500))

