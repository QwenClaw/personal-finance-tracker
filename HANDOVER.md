## 1. What Was Built

This project is a desktop personal finance tracker that lets you manually enter transactions or import them from bank CSV files. It automatically categorizes expenses, displays monthly totals and category breakdowns, and saves all data locally in a simple JSON file. The application runs offline as a single executable and features a modern dark theme for easy viewing.

## 2. Getting Started

**Prerequisites:**
- Python 3.11
- No system dependencies required

**Install command:**
```bash
pip install -r requirements.txt
```

**Run command:**
```bash
python main_window.py
```

**Configuration:**
- No environment variables needed. The application creates and uses a local `transactions.json` file in the same directory for data storage.

## 3. Project Status

| Issue | Title | Status |
|-------|-------|--------|
| #55 | Correct refund handling in DashboardWidget category breakdown | ✅ Done |

## 4. Known Issues

None — all implemented features passed QA review.

## 5. How to Resume

To continue development, run:

    python agency.py --resume personal-finance-tracker --cycles 3

This will pick up open issues and run up to 3 more dev cycles.