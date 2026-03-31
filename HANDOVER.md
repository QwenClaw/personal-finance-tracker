## 1. What Was Built

This project is a personal finance tracker desktop application for Windows. It allows users to manually enter transactions, import bank CSV files with automatic categorization, and view a dashboard with monthly totals and category breakdowns. The application stores all data locally in a JSON file and runs offline without installation. The core features—manual entry, CSV import, and dashboard navigation—were completed and approved in previous cycles.

## 2. Getting Started

**Prerequisites:**
- Python 3.11
- Windows OS (for PySide6 native performance)

**Install command:**
```bash
pip install -r requirements.txt
```

**Run command:**
```bash
python main_window.py
```

**Configuration:**
- The application uses a local JSON file (`transactions.json`) for data storage, created automatically in the same directory as the script.
- No environment variables are required.

## 3. Project Status

| Issue | Title | Status |
|-------|-------|--------|
| #80 | Fix DataStore singleton pattern for QObject compatibility | ⚠️ Needs Rework |
| #81 | Implement proper QObject-compatible singleton pattern for DataStore | ❌ Not Started |
| #83 | Add unit tests for DataStore singleton pattern and QObject compatibility | ❌ Not Started |
| #84 | (Unknown title - not provided in QA report) | ❌ Not Started |

## 4. Known Issues

- The DataStore singleton pattern is not properly implemented for QObject compatibility, causing potential TypeError with multiple instantiations.
- No unit tests exist to verify the singleton behavior or QObject compatibility.
- Issue #84 title is unknown as it was not provided in the QA report.

## 5. How To Resume

To continue development, run:

    python agency.py --resume personal-finance-tracker --cycles 3

This will pick up open issues and run up to 3 more dev cycles.