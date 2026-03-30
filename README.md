# Personal Finance Tracker

A single-file, offline Windows desktop application for individuals in India to manually log expenses, view monthly spending breakdowns by category, and import bank CSVs, without accounts or cloud dependencies.

## Goals

- Enable users to add a transaction in under 30 seconds.
- Provide instant visibility into total monthly spending per category.
- Support offline, private operation with local JSON data storage.
- Simplify expense tracking with pre-defined categories and CSV import.
- Deliver a clean, dark-themed interface with minimal learning curve.

---
## Architecture

- **Python 3.11** with **PySide6** for the desktop GUI, chosen for native Windows performance, single-file compilation via PyInstaller, and a modern dark theme.
- **JSON** for local data storage, providing a simple, human-readable format that requires no database setup.
- **PyInstaller** for compiling the application into a single executable under 20MB, ensuring offline, installation-free operation.

### Project Files

- `main.py` — CLI entry point: compiles the app with PyInstaller and launches the PySide6 main window.
- `app/main_window.py` — Main application window: initializes UI, manages dashboard and transaction views, and handles navigation.
- `app/data_store.py` — Singleton data manager: handles JSON load/save, transaction CRUD, and monthly data queries.
- `app/models/transaction.py` — Transaction dataclass: defines fields, validation, and serialization for a single expense entry.
- `app/services/csv_importer.py` — CSV parser: reads bank CSV, applies keyword-based auto-categorization, and deduplicates transactions.
- `app/ui/dashboard_widget.py` — Dashboard UI: displays monthly totals, category breakdowns, and a text-based bar chart.
- `app/ui/transaction_form_widget.py` — Transaction entry form: provides fields for amount, date, category dropdown, and description.
- `app/ui/month_navigation_widget.py` — Month navigation UI: allows user to switch between months to view historical data.
- `app/utils/constants.py` — Constants: defines pre-defined categories, keyword mappings for CSV import, and default settings.
- `app/utils/helpers.py` — Utility functions: date formatting, amount validation, and text-based chart generation.

_See `architecture.md` for the full design._

---

_Development log will be appended as issues are completed._

## Development Log

### Cycle 1 — #1: Implement Data Store and Transaction Model

**APPROVE** — The implementation meets all acceptance criteria: Data Store class is implemented with required methods, Transaction dataclass includes all fields and validation, JSON path is configurable with default, and auto-save triggers on add_transaction. No critical bugs or missing functionality found.

### Cycle 2 — #2: Build Main Application Window and Dashboard Widget

**REQUEST_CHANGES** — The implementation provides the main window and dashboard widget, but the Dashboard Widget does not display the total monthly spending and category breakdown as required. The dashboard_widget.py file is missing, and the main_window.py file is not provided in the changed files, so the acceptance criteria for dashboard display and navigation arrows cannot be verified.

### Cycle 3 — #3: Create Transaction Form Widget for Manual Entry

**REQUEST_CHANGES** — The Transaction Form Widget implements the required fields and validation, but it does not meet the acceptance criteria for clearing the form after submission. The form clears all fields except the date, which is reset to today's date, but the acceptance criteria require the form to be cleared, which implies resetting all fields to their default state. Additionally, the date validation uses a try-except block that catches all exceptions, which is too broad and may hide specific errors.

### Cycle 4 — #4: Implement CSV Importer with Auto-Categorization

**REQUEST_CHANGES** — The CSV Importer implementation meets most acceptance criteria but has a critical bug: it stores positive amounts for refunds and uses an is_refund flag, which conflicts with the Data Store's expectation of negative amounts for refunds. This will cause incorrect financial calculations in the dashboard.

### Cycle 5 — #5: Integrate UI Components and Finalize Single-File Application

**REQUEST_CHANGES** — The implementation partially meets the acceptance criteria but has critical bugs. The CSV import functionality is missing integration in main_window.py, and the CSVImporter does not handle refunds correctly (stores positive amount but is_refund flag may not be used). Additionally, the build.py file is not provided, so compilation cannot be verified.

### Cycle 6 — #7: Dashboard Widget missing implementation

**REQUEST_CHANGES** — The Dashboard Widget implementation meets most acceptance criteria but has a critical bug: the 'Net Spent' calculation incorrectly subtracts refunds from total spent, which may not align with user expectations for net spending. Additionally, the widget does not subscribe to data changes for real-time updates, violating the acceptance criteria.

### Cycle 7 — #8: Main Window implementation not provided

**APPROVE** — The main_window.py file implements the Main Application Window with all required functionality. It initializes the UI with a transaction form and dashboard, applies the dark theme stylesheet, and handles navigation signals. The implementation meets the acceptance criteria of launching with the dark theme applied.

### Cycle 8 — #10: Fix form clearing logic in Transaction Form Widget

**REQUEST_CHANGES** — The implementation partially meets the acceptance criteria by clearing the amount and description fields and resetting the category dropdown, but the date field reset logic is incorrectly placed outside the try block in the clear_form method, causing a potential indentation error and preventing the success message from displaying. Additionally, the form clearing is not explicitly called after a successful transaction submission in the current code structure.

### Cycle 9 — #11: Improve date validation in Transaction Form Widget

**REQUEST_CHANGES** — The implementation adds specific date format and validity checks, meeting the acceptance criteria. However, the code has a critical bug: the success message and form clearing are incorrectly indented, causing them to execute only if an exception occurs, not on success. This breaks the normal flow.
