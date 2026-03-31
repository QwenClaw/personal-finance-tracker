# AGENTS.md — Project Memory for AI Developers

This file is your **primary reference**. Read it first. It is updated automatically after each QA cycle.

## Project Overview
 Product Brief:  Build a single-file Windows desktop application for personal finance management.  Core Features: 1. Manual transaction entry (amount, date, category, description) 2. Pre-defined categories: Food, Rent, Transport, Entertainment, Shopping, Health, Bills, Other 3. Monthly view showing total spending per category 4. CSV import for bank statements (amount, date, description columns) 5. Dashboard: total spent, top spending category, daily average this month 6. Local save/load to JSON file  Tech Stack: - Python only - Tkinter for GUI (no external dependencies beyond standard library) - Single .py file that compiles to .exe with PyInstaller  UI Design: - Clean, simple interface - Dark theme preferred - Tables for transactions, pie chart or bar chart for monthly breakdown (use matplotlib if needed, otherwise text-based) - Add Transaction' form at top, transaction list in middle, summary at bottom  Interaction Flow: - App opens → Load last saved file or start fresh - User adds transactions manually or imports CSV - Dashboard updates automatically - Auto-saves on every change  Constraints: - No account system, no cloud - Works offline - Must run on Windows 10/11 - File size target: under 20MB when compiled  Generate the complete application. The BA should confirm requirements before dev starts. QA must test every feature before closing.

## Tech Stack & Entry Point
Derived from architecture. Run `python main.py` to start the application.

## Test Commands
```
python -m pytest          # run all tests (if tests/ exists)
python main.py            # smoke-test: must not crash on startup
python -c "import <module>"  # quick import sanity check
```

## Coding Conventions
- Follow the file boundaries defined in architecture.md exactly
- Do not merge multiple architecture files into one
- Each file should be ~100-150 lines; split if larger
- Use descriptive variable names; no single-letter names except loop indices
- Handle all error cases at system boundaries with try/except

## Known Pitfalls


---
*Auto-generated at project setup. Do not delete.*
- **Issue #78 (Fix DataStore __new__ method for QObject compatibility)**: The implementation does not meet all acceptance criteria. The DataStore's __new__ method still uses object.__new__(cls), which is not compatible with QObject subclasses and may cause issues. Additionally, the singleton pattern is not properly managed for QObject, and the code lacks tests for the new
- **Issue #80 (Fix DataStore singleton pattern for QObject compatibility)**: The implementation does not meet all acceptance criteria. The DataStore's __new__ method still calls super().__new__(cls) directly, which can cause TypeError with QObject subclasses. Additionally, the singleton pattern is not properly enforced across multiple instantiations with different json_path
- **Issue #81 (Add unit tests for DataStore singleton and signal functionality)**: The implementation does not include any unit tests for the DataStore class, which is a requirement of the acceptance criteria. The changed file only contains the DataStore implementation, but no test file was added or modified to verify singleton behavior, signal emission, or method correctness.
- **Issue #83 (Implement proper QObject-compatible singleton pattern for DataStore)**: The implementation does not meet all acceptance criteria. The DataStore class uses a custom __new__ method that directly calls super().__new__(cls), which is not QObject-compatible and may cause TypeError. Additionally, the singleton pattern is not properly enforced across multiple instantiations wi
