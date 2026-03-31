from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QFrame, QPushButton, QFileDialog, QMessageBox, QApplication
from PySide6.QtCore import Qt
from dashboard_widget import DashboardWidget
from transaction_form_widget import TransactionFormWidget
from csv_importer import CSVImporter
from data_store import DataStore
import os
import sys


class MainWindow(QMainWindow):
    """Main application window for personal finance management."""
    
    def __init__(self):
        super().__init__()
        self.data_store = DataStore()
        self.data_store.load()  # Load existing transactions
        self.init_ui()
        self.apply_dark_theme()
    
    def init_ui(self):
        """Initialize the user interface."""
        self.setWindowTitle("Personal Finance Manager")
        self.setGeometry(100, 100, 1200, 800)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Create splitter for resizable sections
        splitter = QSplitter(Qt.Vertical)
        
        # Top section: Transaction Form
        self.transaction_form = TransactionFormWidget()
        splitter.addWidget(self.transaction_form)
        
        # Bottom section: Dashboard
        self.dashboard = DashboardWidget()
        self.dashboard.month_changed.connect(self.on_month_changed)
        splitter.addWidget(self.dashboard)
        
        # Set initial sizes (form gets less space)
        splitter.setSizes([200, 600])
        
        main_layout.addWidget(splitter)
        
        # Connect form submission to refresh dashboard
        self.transaction_form.submit_button.clicked.connect(self.refresh_dashboard)
        
        # Add CSV import button
        self.csv_import_button = QPushButton("Import CSV")
        self.csv_import_button.clicked.connect(self.import_csv)
        main_layout.addWidget(self.csv_import_button)
    
    def apply_dark_theme(self):
        """Apply dark theme stylesheet to the application."""
        dark_stylesheet = """
        QMainWindow {
            background-color: #2b2b2b;
            color: #ffffff;
        }
        QWidget {
            background-color: #2b2b2b;
            color: #ffffff;
            font-family: Segoe UI, Arial, sans-serif;
        }
        QLabel {
            color: #ffffff;
        }
        QLineEdit, QComboBox {
            background-color: #3c3f41;
            color: #ffffff;
            border: 1px solid #555555;
            padding: 5px;
            border-radius: 3px;
        }
        QLineEdit:focus, QComboBox:focus {
            border: 1px solid #007acc;
        }
        QPushButton {
            background-color: #007acc;
            color: #ffffff;
            border: none;
            padding: 8px 16px;
            border-radius: 3px;
        }
        QPushButton:hover {
            background-color: #1c97ea;
        }
        QPushButton:pressed {
            background-color: #005a9e;
        }
        QFrame {
            border: 1px solid #555555;
            border-radius: 3px;
        }
        QSplitter::handle {
            background-color: #555555;
        }
        """
        self.setStyleSheet(dark_stylesheet)
    
    def on_month_changed(self, year, month):
        """Handle month change signal from dashboard."""
        # Dashboard already updates itself, but we can add additional logic here
        pass
    
    def refresh_dashboard(self):
        """Refresh the dashboard display."""
        self.dashboard.refresh()

    def import_csv(self):
        """Open file dialog to select CSV file, import transactions, and refresh dashboard."""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Import CSV",
            "",
            "CSV Files (*.csv);;All Files (*)"
        )
        
        if not file_path:
            return  # User cancelled
        
        try:
            csv_importer = CSVImporter()
            transactions = csv_importer.import_csv(file_path)
            
            if not transactions:
                QMessageBox.information(self, "Import", "No transactions found in CSV file.")
                return
            
            # Add transactions to data store
            for transaction in transactions:
                self.data_store.add_transaction(transaction)
            
            # Refresh dashboard
            self.refresh_dashboard()
            
            QMessageBox.information(self, "Import Success", f"Imported {len(transactions)} transactions.")
        
        except Exception as e:
            QMessageBox.critical(self, "Import Error", f"Failed to import CSV: {str(e)}")
