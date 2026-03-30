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
