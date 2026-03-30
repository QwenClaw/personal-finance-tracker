## 1. What Was Built

A desktop personal finance tracker application for Windows that allows users to manually enter transactions and import bank CSV files for automatic categorization. The software provides a dashboard with monthly totals and category breakdowns, stores all data locally in a single JSON file for easy backup, and runs as a single executable under 20MB for offline, installation-free operation. All core features—including manual entry, CSV import, and real-time dashboard updates—have been implemented and passed QA review.

## 2. Getting Started

**Prerequisites:**
- Python 3.11
- System dependencies: PySide6 (installed via pip)

**Install command:**
```bash
pip install -r requirements.txt
```

**Run command:**
```bash
python main_window.py
```

**Configuration:**
- No environment variables needed. The application uses a local `transactions.json` file in the same directory for data storage, which is created automatically on first run.

## 3. Project Status

| Issue | Title | Status |
|-------|-------|--------|
| #33 | Transaction model validation does not allow negative amounts | ✅ Done |

## 4. Known Issues

None — all implemented features passed QA review.

## 5. How to Resume

To continue development, run:

    python agency.py --resume personal-finance-tracker --cycles 3

This will pick up open issues and run up to 3 more dev cycles.