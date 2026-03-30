from PySide6.QtWidgets import (QWidget, QLabel, QLineEdit, QComboBox, QPushButton,
                             QVBoxLayout, QHBoxLayout, QMessageBox)
from PySide6.QtCore import QDate
from transaction_model import Transaction
from data_store import DataStore
import uuid


class TransactionFormWidget(QWidget):
    """Widget for manual transaction entry."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data_store = DataStore()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Amount field
        amount_layout = QHBoxLayout()
        amount_layout.addWidget(QLabel("Amount:"))
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount (positive number)")
        amount_layout.addWidget(self.amount_input)
        layout.addLayout(amount_layout)
        
        # Date field (default today)
        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel("Date:"))
        self.date_input = QLineEdit()
        self.date_input.setText(QDate.currentDate().toString("yyyy-MM-dd"))
        date_layout.addWidget(self.date_input)
        layout.addLayout(date_layout)
        
        # Category dropdown
        category_layout = QHBoxLayout()
        category_layout.addWidget(QLabel("Category:"))
        self.category_combo = QComboBox()
        categories = ["Food", "Rent", "Transport", "Entertainment",
                      "Shopping", "Health", "Bills", "Other"]
        self.category_combo.addItems(categories)
        category_layout.addWidget(self.category_combo)
        layout.addLayout(category_layout)
        
        # Description field
        desc_layout = QHBoxLayout()
        desc_layout.addWidget(QLabel("Description:"))
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Enter description")
        desc_layout.addWidget(self.description_input)
        layout.addLayout(desc_layout)
        
        # Submit button
        self.submit_button = QPushButton("Add Transaction")
        self.submit_button.clicked.connect(self.add_transaction)
        layout.addWidget(self.submit_button)
        
        self.setLayout(layout)
    
    def add_transaction(self):
        """Validate input and add transaction to Data Store."""
        try:
            # Get and validate amount
            amount_str = self.amount_input.text().strip()
            if not amount_str:
                raise ValueError("Amount is required")
            try:
                amount = float(amount_str)
            except ValueError:
                raise ValueError("Amount must be a number")
            if amount <= 0:
                raise ValueError("Amount must be positive")
            
            # Get and validate date
            date_str = self.date_input.text().strip()
            if not date_str:
                raise ValueError("Date is required")
            try:
                # Validate date format
                QDate.fromString(date_str, "yyyy-MM-dd")
            except:
                raise ValueError("Date must be in YYYY-MM-DD format")
            
            # Get category
            category = self.category_combo.currentText()
            
            # Get description
            description = self.description_input.text().strip()
            
            # Create transaction
            transaction = Transaction(
                id=str(uuid.uuid4()),
                amount=amount,
                date=date_str,
                category=category,
                description=description
            )
            
            # Add to data store
            self.data_store.add_transaction(transaction)
            
            # Clear form
            self.clear_form()

    def clear_form(self):
        """Clear all form fields and reset to default state."""
        self.amount_input.clear()
        self.date_input.setText(QDate.currentDate().toString("yyyy-MM-dd"))
        self.category_combo.setCurrentIndex(0)
        self.description_input.clear()
            
            # Show success message
            QMessageBox.information(self, "Success", "Transaction added successfully!")
            
        except ValueError as e:
            QMessageBox.warning(self, "Validation Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {str(e)}")