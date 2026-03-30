# Requirements Document: Personal Finance Tracker

## Project Summary
A single-file, offline Windows desktop application for individuals in India to manually log expenses, view monthly spending breakdowns by category, and import bank CSVs, without accounts or cloud dependencies.

## Goals
- Enable users to add a transaction in under 30 seconds.
- Provide instant visibility into total monthly spending per category.
- Support offline, private operation with local JSON data storage.
- Simplify expense tracking with pre-defined categories and CSV import.
- Deliver a clean, dark-themed interface with minimal learning curve.

## Scope
### In Scope
- Manual transaction entry (amount, date, category, description).
- Pre-defined categories: Food, Rent, Transport, Entertainment, Shopping, Health, Bills, Other.
- Monthly view showing total spending and category-wise breakdown.
- CSV import with keyword-based auto-categorization and duplicate/refund handling.
- Dashboard with key metrics (e.g., total monthly spending, top categories).
- Local JSON data storage with auto-save on every change.
- Single-file Windows desktop application (under 20MB compiled).

### Deferred
- Income tracking and budgeting features.
- Multi-user support or cloud sync.
- Advanced analytics or custom categories.
- Integration with other financial tools or live bank feeds.

## User Stories
1. As a salaried employee, I want to quickly add a transaction with amount, date, and category so that I can log expenses in under 30 seconds without friction.
2. As a freelancer, I want to import my bank CSV and have transactions auto-categorized by keywords so that I can avoid manual entry for bulk data.
3. As a privacy-conscious user, I want all data stored locally in JSON format with auto-save so that my financial information remains offline and private.
4. As a time-constrained user, I want to see a monthly dashboard with total spending and category breakdowns so that I can instantly understand where my money went.
5. As a Windows user, I want a single-file desktop app that runs without internet so that I can track expenses seamlessly in my existing workflow.

## Acceptance Criteria
### Manual Transaction Entry
- User can input amount, date (default to today), category (dropdown of pre-defined list), and description.
- Transaction is saved to local JSON immediately upon entry.
- Entry form is accessible from the main dashboard with a clear "Add Transaction" button.

### Pre-defined Categories
- Categories are fixed to the list: Food, Rent, Transport, Entertainment, Shopping, Health, Bills, Other.
- User can select a category from a dropdown during transaction entry or CSV import.
- No option to add or modify categories in this version.

### Monthly View with Totals
- Dashboard displays current month's total spending and a breakdown by category (e.g., "₹18,000 spent — ₹8,000 on food, ₹5,000 on rent").
- View updates automatically when new transactions are added or CSV is imported.
- User can navigate to previous months to view historical data.

### CSV Import with Auto-Categorization
- User can import a CSV file from bank statements.
- System detects keywords (e.g., "restaurant" → Food, "uber" → Transport) to assign categories.
- Handles duplicates by skipping or merging based on date/amount match; refunds are marked as negative amounts.
- Imported transactions are saved to local JSON and reflected in the dashboard.

### Dashboard with Key Metrics
- Shows total monthly spending, top 3 categories by amount, and a simple text-based chart (e.g., bar chart using characters).
- Metrics update in real-time as transactions are added or imported.
- Dashboard is the default view on app launch.

### Local JSON Storage
- All data is stored in a single JSON file on the user's local machine.
- Auto-save triggers on every transaction add, edit, or import.
- Data persists across app sessions without internet.

### Single-File Windows Application
- Compiled application runs on Windows 10/11 without installation.
- File size is under 20MB.
- No external dependencies or internet required for operation.