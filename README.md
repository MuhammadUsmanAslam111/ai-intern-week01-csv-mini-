# AI Intern Week 01 - CSV Mini Project

This project demonstrates basic CSV data processing using Python and Pandas.  

## Features
- Reads student marks from `student_marks.csv`
- Renames columns for clarity
- Calculates **average marks** for each student
- Saves results to `student_avg.csv`
- Modular functions (`read_csv`, `rename_column`, `calculate_average`, `save_csv`) to allow **unit testing**

## Testing
- `pytest` used for testing all functions
- Sample tests ensure correctness of **renaming, average calculation, and CSV saving**
- Can be run locally to verify green tests

## Usage
1. Clone the repository
2. Ensure `pandas` is installed
3. Run `main.py` to calculate averages
4. Run `pytest test_main.py` to validate functionality

> This mini-project follows best practices for **modular, testable Python code**.
