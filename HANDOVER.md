## 1. What Was Built

A desktop personal finance tracker for Windows that lets you manually enter transactions or import them from bank CSV files. The application automatically categorizes imported transactions using keywords and displays a dashboard with monthly totals and category breakdowns. All data is saved locally in a JSON file for easy backup, and the app runs as a single executable without needing installation.

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
- No environment variables needed. The app creates a `finance_data.json` file in the same directory for data storage on first run.

## 3. Project Status

| Issue | Title | Status |
|-------|-------|--------|
| #68 | Remove QObject inheritance from DataStore to fix singleton error | ✅ Done |

## 4. Known Issues

None — all implemented features passed QA review.

## 5. How to Resume

To continue development, run:

    python agency.py --resume personal-finance-tracker --cycles 3

This will pick up open issues and run up to 3 more dev cycles.