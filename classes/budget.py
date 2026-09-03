# Build a budget calculator
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, destination):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {destination.name}")
        destination.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*")
        lines = [title]
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}"[:7].rjust(7)
            lines.append(description + amount)
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    withdrawals = [
        sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        for category in categories
    ]
    total = sum(withdrawals)
    percentages = [int(amount / total * 100) // 10 * 10 if total else 0 for amount in withdrawals]

    lines = ["Percentage spent by category"]
    for level in range(100, -1, -10):
        row = f"{level:>3}| "
        row += "".join("o  " if percentage >= level else "   " for percentage in percentages)
        lines.append(row)

    lines.append("    " + "-" * (len(categories) * 3 + 1))
    max_name_length = max((len(category.name) for category in categories), default=0)
    for index in range(max_name_length):
        row = "     "
        for category in categories:
            row += (category.name[index] if index < len(category.name) else " ") + "  "
        lines.append(row)

    return "\n".join(lines)
