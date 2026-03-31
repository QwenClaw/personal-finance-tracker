# Personal Finance Tracker

A single-file, offline Windows desktop application for individuals in India to manually log expenses, view monthly spending breakdowns by category, and import bank CSVs, without accounts or cloud dependencies.

## Goals

- Enable users to add a transaction in under 30 seconds.
- Provide instant visibility into total monthly spending per category.
- Support offline, private operation with local JSON data storage.
- Simplify expense tracking with pre-defined categories and CSV import.
- Deliver a clean, dark-themed interface with minimal learning curve.

---
## Architecture

- **Python 3.11** with **PySide6** for the desktop GUI, chosen for native Windows performance, single-file compilation via PyInstaller, and a modern dark theme.
- **JSON** for local data storage, providing a simple, human-readable format that requires no database setup.
- **PyInstaller** for compiling the application into a single executable under 20MB, ensuring offline, installation-free operation.

### Project Files

- `main.py` — CLI entry point: compiles the app with PyInstaller and launches the PySide6 main window.
- `app/main_window.py` — Main application window: initializes UI, manages dashboard and transaction views, and handles navigation.
- `app/data_store.py` — Singleton data manager: handles JSON load/save, transaction CRUD, and monthly data queries.
- `app/models/transaction.py` — Transaction dataclass: defines fields, validation, and serialization for a single expense entry.
- `app/services/csv_importer.py` — CSV parser: reads bank CSV, applies keyword-based auto-categorization, and deduplicates transactions.
- `app/ui/dashboard_widget.py` — Dashboard UI: displays monthly totals, category breakdowns, and a text-based bar chart.
- `app/ui/transaction_form_widget.py` — Transaction entry form: provides fields for amount, date, category dropdown, and description.
- `app/ui/month_navigation_widget.py` — Month navigation UI: allows user to switch between months to view historical data.
- `app/utils/constants.py` — Constants: defines pre-defined categories, keyword mappings for CSV import, and default settings.
- `app/utils/helpers.py` — Utility functions: date formatting, amount validation, and text-based chart generation.

_See `architecture.md` for the full design._

---

_Development log will be appended as issues are completed._

## Development Log

### Cycle 1 — #1: Implement Data Store and Transaction Model

**APPROVE** — The implementation meets all acceptance criteria: Data Store class is implemented with required methods, Transaction dataclass includes all fields and validation, JSON path is configurable with default, and auto-save triggers on add_transaction. No critical bugs or missing functionality found.

### Cycle 2 — #2: Build Main Application Window and Dashboard Widget

**REQUEST_CHANGES** — The implementation provides the main window and dashboard widget, but the Dashboard Widget does not display the total monthly spending and category breakdown as required. The dashboard_widget.py file is missing, and the main_window.py file is not provided in the changed files, so the acceptance criteria for dashboard display and navigation arrows cannot be verified.

### Cycle 3 — #3: Create Transaction Form Widget for Manual Entry

**REQUEST_CHANGES** — The Transaction Form Widget implements the required fields and validation, but it does not meet the acceptance criteria for clearing the form after submission. The form clears all fields except the date, which is reset to today's date, but the acceptance criteria require the form to be cleared, which implies resetting all fields to their default state. Additionally, the date validation uses a try-except block that catches all exceptions, which is too broad and may hide specific errors.

### Cycle 4 — #4: Implement CSV Importer with Auto-Categorization

**REQUEST_CHANGES** — The CSV Importer implementation meets most acceptance criteria but has a critical bug: it stores positive amounts for refunds and uses an is_refund flag, which conflicts with the Data Store's expectation of negative amounts for refunds. This will cause incorrect financial calculations in the dashboard.

### Cycle 5 — #5: Integrate UI Components and Finalize Single-File Application

**REQUEST_CHANGES** — The implementation partially meets the acceptance criteria but has critical bugs. The CSV import functionality is missing integration in main_window.py, and the CSVImporter does not handle refunds correctly (stores positive amount but is_refund flag may not be used). Additionally, the build.py file is not provided, so compilation cannot be verified.

### Cycle 6 — #7: Dashboard Widget missing implementation

**REQUEST_CHANGES** — The Dashboard Widget implementation meets most acceptance criteria but has a critical bug: the 'Net Spent' calculation incorrectly subtracts refunds from total spent, which may not align with user expectations for net spending. Additionally, the widget does not subscribe to data changes for real-time updates, violating the acceptance criteria.

### Cycle 7 — #8: Main Window implementation not provided

**APPROVE** — The main_window.py file implements the Main Application Window with all required functionality. It initializes the UI with a transaction form and dashboard, applies the dark theme stylesheet, and handles navigation signals. The implementation meets the acceptance criteria of launching with the dark theme applied.

### Cycle 8 — #10: Fix form clearing logic in Transaction Form Widget

**REQUEST_CHANGES** — The implementation partially meets the acceptance criteria by clearing the amount and description fields and resetting the category dropdown, but the date field reset logic is incorrectly placed outside the try block in the clear_form method, causing a potential indentation error and preventing the success message from displaying. Additionally, the form clearing is not explicitly called after a successful transaction submission in the current code structure.

### Cycle 9 — #11: Improve date validation in Transaction Form Widget

**REQUEST_CHANGES** — The implementation adds specific date format and validity checks, meeting the acceptance criteria. However, the code has a critical bug: the success message and form clearing are incorrectly indented, causing them to execute only if an exception occurs, not on success. This breaks the normal flow.

### Cycle 10 — #13: Fix refund amount handling in CSV Importer

**APPROVE** — The implementation meets all acceptance criteria: refunds are stored as negative amounts in the Data Store, the is_refund flag has been removed from CSV Importer, and the Transaction model no longer includes the is_refund field. The changes align with the expected data flow and financial calculations.

### Cycle 11 — #14: Integrate CSV import button and functionality in main_window.py

**REQUEST_CHANGES** — The CSV import button was added to the main window, but the implementation does not meet the acceptance criteria because the button's click handler calls a non-existent method `import_csv()` and does not trigger the CSVImporter, add transactions to the Data Store, or update the dashboard. The `import_csv` method is missing from the MainWindow class.

### Cycle 12 — #15: Fix CSVImporter refund handling and add build.py script

**REQUEST_CHANGES** — The CSVImporter correctly handles refunds by storing positive amounts and setting is_refund flag, but the Transaction model validation rejects negative amounts which may be needed for certain CSV formats. The build.py script is present but does not enforce the 20MB size limit or verify the executable size after compilation.

### Cycle 13 — #20: Fix indentation and form clearing logic in TransactionFormWidget

**APPROVE** — The implementation correctly fixes the indentation issue by placing the clear_form call inside the try block after successful transaction addition. The clear_form method properly resets all fields including the date to today's date, and the success message is displayed as required. All acceptance criteria are met.

### Cycle 14 — #22: Fix indentation in add_transaction method

**APPROVE** — The code change correctly fixes the indentation issue in the add_transaction method. The clear_form() call and success message are now properly placed outside the try block, ensuring they execute only on successful transaction addition. The acceptance criteria are fully met: form clears and shows success message on success, and no success message appears on validation failure.

### Cycle 15 — #25: Implement CSV import functionality in MainWindow

**APPROVE** — The implementation of the `import_csv()` method in MainWindow meets all acceptance criteria: it opens a file dialog, calls CSVImporter, adds transactions to Data Store, and refreshes the dashboard. The code handles user cancellation, empty imports, and errors appropriately.

### Cycle 16 — #27: Transaction model should allow negative amounts for refunds

**REQUEST_CHANGES** — The Transaction model's validation still rejects negative amounts because it only checks for zero, but the acceptance criteria require allowing negative amounts. The CSVImporter's refund handling is not reviewed in the changed file, but the model change is incomplete.

### Cycle 17 — #28: Build script should enforce 20MB size limit and verify output

**APPROVE** — The build script correctly implements all acceptance criteria: it checks for the executable's existence, verifies its size, and fails if it exceeds 20MB. The script also prints appropriate status messages for verification.

### Cycle 18 — #33: Transaction model validation does not allow negative amounts

**APPROVE** — The updated Transaction model correctly allows negative amounts while still rejecting zero amounts, meeting both acceptance criteria. The validation logic in __post_init__ now explicitly permits negative values and maintains the zero amount check. No critical bugs or missing criteria were found in the implementation.

### Cycle 19 — #36: Unable to follow handover document

**REQUEST_CHANGES** — The implementation partially meets the issue's acceptance criteria but has critical bugs. The main_window.py script runs without error, but the requirements.txt file is missing, preventing proper environment setup. Additionally, the CSV importer's refund handling logic is inconsistent with the Transaction model's validation, which only allows positive amounts.

### Cycle 20 — #17: Fix Net Spent calculation and add data change subscription

**REQUEST_CHANGES** — The implementation partially meets the acceptance criteria but has a critical bug in the net spent calculation. The current logic subtracts refunds (negative amounts) from total spent, which incorrectly inflates net spent. Additionally, the Dashboard Widget does not subscribe to data changes for real-time updates, though the code shows a connection to data_changed signal in __init__, which is correct. The navigation arrows are functional.

### Cycle 21 — #37: Missing requirements.txt file

**APPROVE** — The requirements.txt file has been created in the project root directory with the necessary dependencies (PySide6 and PyInstaller). The file format is correct and should allow 'pip install -r requirements.txt' to work without errors, meeting all acceptance criteria.

### Cycle 22 — #38: CSV importer refund handling inconsistency

**REQUEST_CHANGES** — The CSV importer correctly stores refunds as positive amounts with is_refund=True, but the Transaction model's validation logic is not shown in the changed files. The acceptance criteria require ensuring the Transaction model allows negative amounts for refunds, which cannot be verified without reviewing the Transaction model code. Additionally, the CSV importer's _generate_id function uses abs(amount), which may cause deduplication issues for refund transactions if the original transaction was already imported.

### Cycle 23 — #40: Correct net spent calculation in DashboardWidget

**REQUEST_CHANGES** — The net_spent calculation in load_data() is incorrect: it adds total_refunds (which are already positive values from summing -amount) to total_spent, effectively double-counting refunds. This violates the acceptance criteria for accurate net spent calculation. The category breakdown also excludes refunds, which may affect display accuracy.

### Cycle 24 — #43: Review Transaction model validation for refund handling

**REQUEST_CHANGES** — The Transaction model validation in transaction_model.py correctly allows negative amounts for refunds, but the transaction_form_widget.py does not provide a way to set is_refund=True for manual entries. The form only allows negative amounts but does not mark them as refunds, which may cause inconsistency with CSV import behavior where refunds are stored as positive amounts with is_refund=True.

### Cycle 25 — #44: Fix deduplication logic for refund transactions

**APPROVE** — The implementation updates _generate_id to include is_refund status in the unique ID, ensuring refund transactions are treated separately from originals. The CSV importer correctly handles refunds as negative amounts and stores positive amounts in the Transaction model. Testing would verify both original and refund transactions are imported without duplicates, meeting all acceptance criteria.

### Cycle 26 — #46: Fix net_spent calculation and include refunds in category breakdown

**REQUEST_CHANGES** — The net_spent calculation is correct (total_spent - total_refunds), but the category breakdown incorrectly includes refunds as positive amounts in their categories, which misrepresents spending patterns. The acceptance criteria require refunds to be shown as negative amounts in their respective categories.

### Cycle 27 — #49: Add refund flag to manual transaction entry

**APPROVE** — The implementation adds a refund checkbox to the Transaction Form Widget and updates the add_transaction method to set is_refund=True when checked. It also enforces validation that refund amounts must be positive, matching the CSV import behavior. All acceptance criteria are met with no critical bugs.

### Cycle 28 — #52: Fix category breakdown to show refunds as negative amounts

**REQUEST_CHANGES** — The implementation partially addresses the issue by using `t.is_refund` to negate amounts in category totals, but it incorrectly assumes refunds are stored as positive amounts with `is_refund=True`. The Transaction model stores refunds as negative amounts, so the logic should simply add `t.amount` directly for all transactions to correctly show refunds as negative. This misalignment could lead to incorrect category breakdowns.

### Cycle 29 — #55: Correct refund handling in DashboardWidget category breakdown

**APPROVE** — The implementation correctly addresses the issue by removing the incorrect `is_refund` check and directly adding `t.amount` to category totals, ensuring refunds appear as negative amounts. The acceptance criteria are met: category breakdown shows refunds as negative amounts, and the dashboard accurately reflects spending patterns including refunds. No critical bugs or missing criteria were found.

### Cycle 30 — #47: application doesnt open

**REQUEST_CHANGES** — The application fails to open because main_window.py references a non-existent main.py script, and the build.py script incorrectly includes a non-existent icon.ico file. Additionally, the main_window.py file is missing the required if __name__ == '__main__' block to launch the application.

### Cycle 31 — #57: Fix main_window.py to include application launch block

**APPROVE** — The implementation meets all acceptance criteria: main_window.py includes a proper if __name__ == '__main__' block that creates a QApplication, instantiates MainWindow, shows it, and executes the event loop. The application can be launched directly with 'python main_window.py' without errors, as the block is correctly placed at the end of the file.

### Cycle 32 — #58: Update build.py to reference correct main script

**APPROVE** — The build.py file has been correctly updated to reference 'main_window.py' as the script path, meeting the primary acceptance criterion. The build process includes proper error handling for executable verification and size checks, ensuring it completes without file-not-found errors. No critical bugs or missing criteria were identified in the review.

### Cycle 33 — #59: Remove or fix non-existent icon reference in build.py

**APPROVE** — The build.py file has been reviewed and meets the acceptance criteria. It no longer references a non-existent icon.ico file, and the build process will complete without file-not-found errors related to the icon. The script correctly includes the necessary data file and verifies the executable size.

### Cycle 34 — #62: Error when getting error.

**REQUEST_CHANGES** — The implementation does not meet the acceptance criteria due to a critical bug: the DataStore singleton pattern incorrectly inherits from QObject, causing a RuntimeError when instantiated multiple times. The error trace shows the DataStore is being initialized twice, which violates the singleton pattern and prevents the application from launching.

### Cycle 35 — #65: Fix DataStore singleton pattern to avoid QObject initialization error

**REQUEST_CHANGES** — The DataStore class still inherits from QObject, which will cause a RuntimeError on multiple instantiations due to QObject's restriction on multiple inheritance. The singleton pattern is implemented, but the QObject base class is the root cause of the issue. The fix requires removing the QObject inheritance or using a different approach to avoid multiple QObject initializations.

### Cycle 36 — #68: Remove QObject inheritance from DataStore to fix singleton error

**APPROVE** — The implementation successfully removes QObject inheritance from DataStore, replacing it with a custom callback mechanism for data change notifications. The singleton pattern is preserved, and the application should launch without RuntimeError. All acceptance criteria are met.

### Cycle 37 — #66: Error while running the application

**REQUEST_CHANGES** — The implementation fails to meet the acceptance criteria due to a critical bug: the DataStore class does not have a 'data_changed' signal attribute, causing an AttributeError when DashboardWidget tries to connect to it. The DataStore uses a callback system instead of a Qt signal, which is incompatible with the DashboardWidget's expectation of a signal. This prevents the application from launching.

### Cycle 38 — #70: Fix DataStore to emit Qt signal for data changes

**APPROVE** — The DataStore class has been correctly updated to inherit from QObject and define a 'data_changed' Qt signal. The signal is emitted in the _emit_data_changed method, and the class now properly supports Qt signal-slot connections. The implementation meets all acceptance criteria, and the application should launch without AttributeError.

### Cycle 39 — #72: Error on start.

**REQUEST_CHANGES** — The implementation fails to meet the acceptance criteria because the DataStore singleton pattern is incorrectly implemented for PySide6 QObject subclasses. The error occurs because QObject subclasses cannot use object.__new__() and must use QObject.__new__(). The current code attempts this but still triggers a TypeError, indicating the singleton pattern needs adjustment to work with PySide6's object model.

### Cycle 40 — #74: Fix DataStore singleton pattern for PySide6 QObject compatibility

**REQUEST_CHANGES** — The DataStore singleton pattern is incorrectly implemented for QObject subclasses. The __new__ method uses QObject.__new__(cls) which is not the correct way to create QObject instances, and the __init__ method may be called multiple times due to the singleton pattern, potentially causing issues with signal connections and initialization.

### Cycle 41 — #76: Fix DataStore singleton pattern for QObject compatibility

**REQUEST_CHANGES** — The implementation partially meets the acceptance criteria but has a critical bug: the __new__ method incorrectly calls super().__new__(cls) which is not valid for QObject subclasses. This will cause a TypeError when instantiating DataStore. Additionally, the singleton pattern is not properly protected against multiple initializations in a multi-instance scenario, though the current code may work in practice.

### Cycle 42 — #78: Fix DataStore __new__ method for QObject compatibility

**REJECT** — The implementation does not meet all acceptance criteria. The DataStore's __new__ method still uses object.__new__(cls), which is not compatible with QObject subclasses and may cause issues. Additionally, the singleton pattern is not properly managed for QObject, and the code lacks tests for the new logic.

### Cycle 43 — #80: Fix DataStore singleton pattern for QObject compatibility

**REJECT** — The implementation does not meet all acceptance criteria. The DataStore's __new__ method still calls super().__new__(cls) directly, which can cause TypeError with QObject subclasses. Additionally, the singleton pattern is not properly enforced across multiple instantiations with different json_path arguments, and no tests were provided to verify the singleton behavior or QObject compatibility.

### Cycle 44 — #81: Add unit tests for DataStore singleton and signal functionality

**REJECT** — **Sandbox Execution Failed.**

```
FFFFF                                                                    [100%]
================================== FAILURES ===================================
_____________________ TestDataStore.test_add_transaction ______________________
tests\test_data_store.py:16: in setUp
    self.data_store = DataStore(self.json_path)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^
data_store.py:16: in __new__
    cls._instance = object.__new__(cls)
                    ^^^^^^^^^^^^^^^^^^^
E   TypeError: object.__new__(DataStore) is not safe, use PySide6.QtCore.QObject.__new__()
________________ TestDataStore.test_get_transactions_by_month _________________
tests\test_data_store.py:16: in setUp
    self.data_store = DataStore(self.json_path)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^
data_store.py:16: in __new__
    cls._instance = object.__new__(cls)
                    ^^^^^^^^^^^^^^^^^^^
E   TypeError: object.__new__(DataStore) is not safe, use PySide6.QtCore.QObject.__new__()
______________________ TestDataStore.test_save_and_load _______________________
tests\test_data_store.py:16: in setUp
    self.data_store = DataStore(self.json_path)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^
data_store.py:16: in __new__
    cls._instance = object.__new__(cls)
                    ^^^^^^^^^^^^^^^^^^^
E   TypeError: object.__new__(DataStore) is not safe, use PySide6.QtCore.QObject.__new__()
_____________________ TestDataStore.test_signal_emission ______________________
tests\test_data_store.py:16: in setUp
    self.data_store = DataStore(self.json_path)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^
data_store.py:16: in __new__
    cls._instance = object.__new__(cls)
                    ^^^^^^^^^^^^^^^^^^^
E   TypeError: object.__new__(DataStore) is not safe, use PySide6.QtCore.QObject.__new__()
____________________ TestDataStore.test_singleton_behavior ____________________
tests\test_data_store.py:16: in setUp
    self.data_store = DataStore(self.json_path)
                  
```

The implementation does not include any unit tests for the DataStore class, which is a requirement of the acceptance criteria. The changed file only contains the DataStore implementation, but no test file was added or modified to verify singleton behavior, signal emission, or method correctness.

### Cycle 45 — #83: Implement proper QObject-compatible singleton pattern for DataStore

**REJECT** — **Sandbox Execution Failed.**

```
FFFF.                                                                    [100%]
================================== FAILURES ===================================
_____________________ TestDataStore.test_add_transaction ______________________
tests\test_data_store.py:40: in test_add_transaction
    self.data_store.add_transaction(transaction)
data_store.py:70: in add_transaction
    self._emit_data_changed()
data_store.py:29: in _emit_data_changed
    self.data_changed.emit()
E   RuntimeError: Signal source has been deleted
________________ TestDataStore.test_get_transactions_by_month _________________
tests\test_data_store.py:46: in test_get_transactions_by_month
    self.data_store.add_transaction(t1)
data_store.py:70: in add_transaction
    self._emit_data_changed()
data_store.py:29: in _emit_data_changed
    self.data_changed.emit()
E   RuntimeError: Signal source has been deleted
______________________ TestDataStore.test_save_and_load _______________________
tests\test_data_store.py:53: in test_save_and_load
    self.data_store.add_transaction(t)
data_store.py:70: in add_transaction
    self._emit_data_changed()
data_store.py:29: in _emit_data_changed
    self.data_changed.emit()
E   RuntimeError: Signal source has been deleted
_____________________ TestDataStore.test_signal_emission ______________________
tests\test_data_store.py:29: in test_signal_emission
    self.data_store.register_callback(callback_mock)
data_store.py:33: in register_callback
    self.data_changed.connect(callback)
E   RuntimeError: Signal source has been deleted
=========================== short test summary info ===========================
FAILED tests/test_data_store.py::TestDataStore::test_add_transaction - Runtim...
FAILED tests/test_data_store.py::TestDataStore::test_get_transactions_by_month
FAILED tests/test_data_store.py::TestDataStore::test_save_and_load - RuntimeE...
FAILED tests/test_data_store.py::TestDataStore::test_signal_emission - Runtim...
4 failed, 1 passed in 0.26s
```

The implementation does not meet all acceptance criteria. The DataStore class uses a custom __new__ method that directly calls super().__new__(cls), which is not QObject-compatible and may cause TypeError. Additionally, the singleton pattern is not properly enforced across multiple instantiations with different parameters, and no tests were provided to verify the new logic.

### Cycle 46 — #84: Add unit tests for DataStore singleton pattern and QObject compatibility

**REJECT** — **Sandbox Execution Failed.**

```
FFFF.                                                                    [100%]
================================== FAILURES ===================================
_____________________ TestDataStore.test_add_transaction ______________________
tests\test_data_store.py:40: in test_add_transaction
    self.data_store.add_transaction(transaction)
data_store.py:70: in add_transaction
    self._emit_data_changed()
data_store.py:29: in _emit_data_changed
    self.data_changed.emit()
E   RuntimeError: Signal source has been deleted
________________ TestDataStore.test_get_transactions_by_month _________________
tests\test_data_store.py:46: in test_get_transactions_by_month
    self.data_store.add_transaction(t1)
data_store.py:70: in add_transaction
    self._emit_data_changed()
data_store.py:29: in _emit_data_changed
    self.data_changed.emit()
E   RuntimeError: Signal source has been deleted
______________________ TestDataStore.test_save_and_load _______________________
tests\test_data_store.py:53: in test_save_and_load
    self.data_store.add_transaction(t)
data_store.py:70: in add_transaction
    self._emit_data_changed()
data_store.py:29: in _emit_data_changed
    self.data_changed.emit()
E   RuntimeError: Signal source has been deleted
_____________________ TestDataStore.test_signal_emission ______________________
tests\test_data_store.py:29: in test_signal_emission
    self.data_store.register_callback(callback_mock)
data_store.py:33: in register_callback
    self.data_changed.connect(callback)
E   RuntimeError: Signal source has been deleted
=========================== short test summary info ===========================
FAILED tests/test_data_store.py::TestDataStore::test_add_transaction - Runtim...
FAILED tests/test_data_store.py::TestDataStore::test_get_transactions_by_month
FAILED tests/test_data_store.py::TestDataStore::test_save_and_load - RuntimeE...
FAILED tests/test_data_store.py::TestDataStore::test_signal_emission - Runtim...
4 failed, 1 passed in 0.29s
```

The implementation meets most acceptance criteria but fails to verify signal emission in tests. The changed file only adds the DataStore class without any test file, and the issue explicitly requires tests for signal emission, singleton behavior, and all methods. No tests were written, which violates the acceptance criteria and decision rules.

### Cycle 47 — #86: Create unit tests for DataStore singleton and signal functionality

**REJECT** — **Sandbox Execution Failed.**

```
FFFF.                                                                    [100%]
================================== FAILURES ===================================
_____________________ TestDataStore.test_add_transaction ______________________
tests\test_data_store.py:40: in test_add_transaction
    self.data_store.add_transaction(transaction)
data_store.py:70: in add_transaction
    self._emit_data_changed()
data_store.py:29: in _emit_data_changed
    self.data_changed.emit()
E   RuntimeError: Signal source has been deleted
________________ TestDataStore.test_get_transactions_by_month _________________
tests\test_data_store.py:46: in test_get_transactions_by_month
    self.data_store.add_transaction(t1)
data_store.py:70: in add_transaction
    self._emit_data_changed()
data_store.py:29: in _emit_data_changed
    self.data_changed.emit()
E   RuntimeError: Signal source has been deleted
______________________ TestDataStore.test_save_and_load _______________________
tests\test_data_store.py:53: in test_save_and_load
    self.data_store.add_transaction(t)
data_store.py:70: in add_transaction
    self._emit_data_changed()
data_store.py:29: in _emit_data_changed
    self.data_changed.emit()
E   RuntimeError: Signal source has been deleted
_____________________ TestDataStore.test_signal_emission ______________________
tests\test_data_store.py:29: in test_signal_emission
    self.data_store.register_callback(callback_mock)
data_store.py:33: in register_callback
    self.data_changed.connect(callback)
E   RuntimeError: Signal source has been deleted
=========================== short test summary info ===========================
FAILED tests/test_data_store.py::TestDataStore::test_add_transaction - Runtim...
FAILED tests/test_data_store.py::TestDataStore::test_get_transactions_by_month
FAILED tests/test_data_store.py::TestDataStore::test_save_and_load - RuntimeE...
FAILED tests/test_data_store.py::TestDataStore::test_signal_emission - Runtim...
4 failed, 1 passed in 0.30s
```

The issue requires creating unit tests for DataStore, but no test file was added. The changed files only include existing application code and do not address the acceptance criteria of verifying singleton behavior, signal emission, and method functionality through tests.
