## 1. What Was Built

This project is a personal finance tracker desktop application for Windows. It allows users to manually enter transactions, import bank CSV files with automatic categorization, and view a dashboard with monthly totals and category breakdowns. The application stores all data locally in a JSON file and runs offline without installation. During this development cycle, the core features for data entry, CSV import, and dashboard visualization were completed, but a calculation error in the net spent amount was identified and requires a fix.

## 2. Getting Started

**Prerequisites:**
- Python 3.11
- Windows OS (for native performance)

**Install command:**
```bash
pip install -r requirements.txt
```

**Run command:**
```bash
python main_window.py
```

**Configuration:**
No environment variables are needed. The application uses a local JSON file (`transactions.json`) for data storage, which will be created automatically in the same directory as the script.

## 3. Project Status

| Issue | Title | Status |
|-------|-------|--------|
| #40 | Correct net spent calculation in DashboardWidget | ⚠️ Needs Rework |
| #43 | Fix net_spent calculation and include refunds in category breakdown | ❌ Not Started |
| #44 | Fix net_spent calculation and include refunds in category breakdown | ❌ Not Started |
| #46 | Fix net_spent calculation and include refunds in category breakdown | ❌ Not Started |

## 4. Known Issues

- The net_spent calculation in the DashboardWidget is incorrect: it double-counts refunds by adding total_refunds (already positive) to total_spent.
- The category breakdown in the dashboard excludes refunds, which may affect display accuracy.

## 5. How To Resume

To continue development, run:

    python agency.py --resume personal-finance-tracker --cycles 3

This will pick up open issues and run up to 3 more dev cycles.