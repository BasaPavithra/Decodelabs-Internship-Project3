import sys

# Ensure UTF-8 encoding for standard output to support the '₹' symbol on all terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def format_currency(amount):
    """Format the number as currency, removing decimals if it's a whole number."""
    if amount == int(amount):
        return f"₹{int(amount)}"
    return f"₹{amount:.2f}"

def get_expense():
    """Prompt the user for an expense amount and return the trimmed input."""
    return input("Enter an expense amount (or type 'quit' to end): ").strip()

def add_expense(expenses_list, amount):
    """Add the expense amount to the expenses list."""
    expenses_list.append(amount)

def display_total(total_amount):
    """Display the current running total."""
    print(f"Current Total: {format_currency(total_amount)}")

def display_summary(expenses_list, total_amount):
    """Calculate and display the final expense summary."""
    print("\nExpense Tracking Summary")
    print("-" * 24)
    
    if not expenses_list:
        print("No expenses were entered.")
        return

    count = len(expenses_list)
    average = total_amount / count
    highest = max(expenses_list)
    lowest = min(expenses_list)

    print(f"Total Spent: {format_currency(total_amount)}")
    print(f"Expenses Added: {count}")
    print(f"Average Expense: {format_currency(average)}")
    print(f"Highest Expense: {format_currency(highest)}")
    print(f"Lowest Expense: {format_currency(lowest)}")
    
    print("\nExpenses:")
    for expense in expenses_list:
        if expense == int(expense):
            print(int(expense))
        else:
            print(expense)

def main():
    """Main execution function for the Expense Tracker."""
    expenses = []
    total = 0.0

    print("Welcome to the Expense Tracker!")
    print("-------------------------------")

    while True:
        user_input = get_expense()
        
        # Sentinel value to exit the loop
        if user_input.lower() == 'quit':
            break
            
        try:
            # Type Conversion
            expense_value = float(user_input)
            
            # Validation for negative expenses (optional but good practice)
            if expense_value < 0:
                print("Expense cannot be negative. Please enter a valid positive number.")
                continue
            
            # Accumulate and record
            add_expense(expenses, expense_value)
            total += expense_value
            
            # Display running total
            display_total(total)
            
        except ValueError:
            # Exception Handling
            print("Invalid input! Please enter a valid number.")

    # Output Phase
    display_summary(expenses, total)

if __name__ == "__main__":
    main()
