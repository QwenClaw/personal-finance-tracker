## 1. What Was Built

A personal finance tracker desktop application for Windows that allows users to manually enter transactions and import bank CSV files. The software automatically categorizes transactions using keywords, stores all data locally in a JSON file, and displays a dashboard with monthly totals and category breakdowns. The application is compiled into a single executable for easy, offline use.

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
- No environment variables are required. The application uses a local `transactions.json` file for data storage, which will be created automatically on first run.

## 3. Project Status

| Issue | Title | Status |
|-------|-------|--------|
| #59 | Remove or fix non-existent icon reference in build.py | ✅ Done |

## 4. Known Issues

None — all implemented features passed QA review.

## 5. How to Resume

This section is omitted because all issues are done and no issues remain.