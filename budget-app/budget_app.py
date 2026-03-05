** start of main.py **

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{'*' * ((30 - len(self.name)) // 2)}{self.name}{'*' * ((30 - len(self.name)) // 2)}"
        output = [title]
        total = 0
        for item in self.ledger:
            desc = item['description'][:23]
            amt = "{:.2f}".format(item['amount'])[-7:]
            output.append(f"{desc:<23}{amt:>7}")
            total += item['amount']
        output.append(f"Total: {total:.2f}")
        return '\n'.join(output)


def create_spend_chart(categories):
    category_names = [category.name for category in categories]
    withdrawals = [sum(item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories]
    total_withdrawals = sum(withdrawals)
    percentages = [int((withdrawal / total_withdrawals) * 100) for withdrawal in withdrawals]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(name) for name in category_names)
    for i in range(max_len):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart


** end of main.py **

