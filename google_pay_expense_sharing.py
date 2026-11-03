class ExpenseSharing:
    def __init__(self, friends):
        self.friends = friends
        self.expenses = {friend: 0.0 for friend in friends}

    def add_expense(self, payer, amount, participants):
        if payer not in self.friends:
            print(f"Error: {payer} is not in the friends list.")
            return

        if not participants:
            print("Error: Participants list cannot be empty.")
            return

        if any(person not in self.friends for person in participants):
            print("Error: All participants must be in the friends list.")
            return

        if len(set(participants)) != len(participants):
            print("Error: Duplicate participants are not allowed.")
            return

        if payer not in participants:
            print("Error: The payer must be included in participants.")
            return

        if amount <= 0:
            print("Error: Amount must be greater than zero.")
            return

        # Calculate each person's share
        split_amount = amount / len(participants)

        # Update each person's net balance
        for participant in participants:
            if participant == payer:
                self.expenses[participant] += amount - split_amount
            else:
                self.expenses[participant] -= split_amount

    def calculate_settlement(self):
        print("\nFinal Settlement:")

        for friend, balance in self.expenses.items():
            if balance > 0.01:
                print(
                    f"{friend} needs to be reimbursed: "
                    f"Rs. {balance:.2f}"
                )
            elif balance < -0.01:
                print(
                    f"{friend} owes: "
                    f"Rs. {-balance:.2f}"
                )
            else:
                print(f"{friend} is settled up.")


if __name__ == "__main__":
    friends = ["Alice", "Bob", "Carol"]

    expense_sharing = ExpenseSharing(friends)

    # Add sample expenses
    expense_sharing.add_expense(
        "Alice", 100, ["Alice", "Bob", "Carol"]
    )
    expense_sharing.add_expense(
        "Bob", 200, ["Alice", "Bob", "Carol"]
    )
    expense_sharing.add_expense(
        "Carol", 150, ["Alice", "Bob", "Carol"]
    )

    # Calculate final settlement
    expense_sharing.calculate_settlement()
