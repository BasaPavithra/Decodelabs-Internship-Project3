# Expense Tracker

## Description
A simple, beginner-friendly command-line application to track personal expenses. The program allows users to continuously enter expenses, maintains a running total, and provides a detailed statistical summary upon exiting. 

## Features
- **Continuous Entry**: Keep adding expenses until you are done.
- **Running Total**: Displays the updated total after every successful entry.
- **Input Validation**: Gracefully handles invalid inputs (like text) without crashing.
- **Expense Counter**: Tracks the total number of expenses entered.
- **Statistical Summary**: Calculates and displays the average, highest, and lowest expenses.
- **Expense History**: Shows a complete list of all recorded expenses at the end.

## Technologies Used
- **Python 3**: Core programming language.

## Concepts Demonstrated
- Variables & Data Types
- User Input & Type Conversion
- `while` Loops & Sentinel Values
- Conditional Statements (`if/else`)
- The Accumulator Pattern
- Exception Handling (`try-except`)
- Functions & Modular Code
- Lists for Data Storage

## How to Run

1. Make sure you have Python 3 installed on your system.
2. Clone this repository or download the project files.
3. Open a terminal or command prompt and navigate to the project directory:
   ```bash
   cd expense_tracker
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Sample Output

```text
Welcome to the Expense Tracker!
-------------------------------
Enter an expense amount (or type 'quit' to end): 100
Current Total: ₹100
Enter an expense amount (or type 'quit' to end): abc
Invalid input! Please enter a valid number.
Enter an expense amount (or type 'quit' to end): 50.5
Current Total: ₹150.50
Enter an expense amount (or type 'quit' to end): 20
Current Total: ₹170.50
Enter an expense amount (or type 'quit' to end): 75
Current Total: ₹245.50
Enter an expense amount (or type 'quit' to end): quit

Expense Tracking Summary
------------------------
Total Spent: ₹245.50
Expenses Added: 4
Average Expense: ₹61.38
Highest Expense: ₹100
Lowest Expense: ₹20

Expenses:
100
50.5
20
75
```
