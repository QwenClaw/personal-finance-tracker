## 1. What Was Built

A desktop personal finance tracker that lets you manually enter transactions or import them from a bank CSV file. The application displays a dashboard with monthly totals and category breakdowns, and automatically saves all data to a local JSON file. All core features—including manual entry, CSV import, and real-time dashboard updates—have been implemented and approved.

## 2. Getting Started

**Prerequisites:**
- Python 3.11
- System dependencies: None (PySide6 and PyInstaller are pure Python)

**Install command:**
```bash
pip install -r requirements.txt
```

**Run command:**
```bash
python main_window.py
```

**Configuration:**
No environment variables are required. The application uses a local `transactions.json` file for data storage, which will be created automatically on first run.

## 3. Project Status

| Issue | Title | Status |
|-------|-------|--------|
| #70 | Fix DataStore to emit Qt signal for data changes | ✅ Done |

## 4. Known Issues

None — all implemented features passed QA review.

## 5. How to Resume

To continue development, run:

    python agency.py --resume personal-finance-tracker --cycles 3

This will pick up open issues and run up to 3 more dev cycles.