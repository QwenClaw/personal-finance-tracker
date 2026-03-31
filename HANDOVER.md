## 1. What Was Built

A desktop personal finance tracker application for Windows that allows users to manually enter transactions and import bank CSV files for automatic categorization. The software provides a dashboard with monthly totals and category breakdowns, stores all data locally in a single JSON file for easy backup, and can be compiled into a standalone executable for offline use. All core features for tracking income and expenses have been implemented and passed QA review.

## 2. Getting Started

**Prerequisites:**
- Python 3.11
- System dependencies: None (PySide6 will install required Qt libraries)

**Install command:**
```bash
pip install -r requirements.txt
```

**Run command:**
```bash
python main_window.py
```

**Configuration:**
- No environment variables needed. The application creates and uses a local `finance_data.json` file in the same directory for data storage.

## 3. Project Status

| Issue | Title | Status |
|-------|-------|--------|
| #58 | Update build.py to reference correct main script | ✅ Done |
| #59 | (Open issue - title not provided) | ❌ Not Started |

## 4. Known Issues

None — all implemented features passed QA review.

## 5. How to Resume

To continue development, run:

    python agency.py --resume personal-finance-tracker --cycles 3

This will pick up open issues and run up to 3 more dev cycles.