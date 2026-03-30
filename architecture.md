## Tech Stack
- **Python 3.11** with **PySide6** for the desktop GUI, chosen for native Windows performance, single-file compilation via PyInstaller, and a modern dark theme.
- **JSON** for local data storage, providing a simple, human-readable format that requires no database setup.
- **PyInstaller** for compiling the application into a single executable under 20MB, ensuring offline, installation-free operation.

## Component Design
- **Main Application Window**: The root GUI component, responsible for initializing the UI, managing the dashboard and transaction views, and handling user navigation. It connects to the Data Store for persistence and the CSV Importer for file operations.
- **Data Store**: A singleton class that manages all data operations (load, save, add transaction, get monthly data). It uses a local JSON file and provides methods for querying transactions by month and category.
- **Transaction Model**: A dataclass representing a single transaction with fields: id, amount, date, category, description, and is_refund. It includes validation logic for amount and date.
- **CSV Importer**: A utility that reads bank CSV files, parses rows, applies keyword-based auto-categorization, and deduplicates transactions. It returns a list of Transaction objects for bulk insertion.
- **Dashboard Widget**: A UI component that displays monthly totals, category breakdowns, and a simple text-based bar chart. It subscribes to data changes to update in real-time.
- **Transaction Form Widget**: A UI component for manual entry, with fields for amount, date (default today), category dropdown, and description. It validates input and triggers a save via the Data Store.

## Data Flow
1. **App Launch**: Main Window loads, initializes Data Store (reads JSON), and displays the Dashboard.
2. **Manual Entry**: User fills the Transaction Form → Form validates input → Data Store adds transaction and auto-saves JSON → Dashboard updates.
3. **CSV Import**: User selects CSV → CSV Importer parses, categorizes, deduplicates → Data Store bulk-adds transactions and auto-saves → Dashboard updates.
4. **Monthly Navigation**: User clicks month arrows → Dashboard queries Data Store for that month's data → UI refreshes with new totals and breakdown.

## Key Design Decisions
- **Single-File JSON Storage**: All data in one file for simplicity and easy backup; auto-save on every change ensures no data loss.
- **Keyword-Based Categorization**: Uses a fixed mapping of keywords to pre-defined categories for fast, rule-based CSV import without ML overhead.
- **Dark Theme by Default**: Applied via PySide6 stylesheets for a modern, low-eye-strain interface that meets user expectations.
- **No Edit/Delete in UI**: To keep scope minimal, transactions are immutable after entry; refunds are handled as negative amounts during import.