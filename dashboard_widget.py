from PySide6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton,
                             QFrame, QTextEdit, QScrollArea)
from PySide6.QtCore import QDate, Signal
from data_store import DataStore
from transaction_model import Transaction
from datetime import datetime
from collections import defaultdict


class DashboardWidget(QWidget):
    """Widget for displaying dashboard with monthly totals, category breakdown, and bar chart."""
    
    # Signal to notify parent of month change
    month_changed = Signal(int, int)  # year, month
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data_store = DataStore()
        self.current_year = QDate.currentDate().year()
        self.current_month = QDate.currentDate().month()
        self.init_ui()
        self.load_data()
        self.data_store.register_callback(self.refresh)
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Month navigation header
        nav_layout = QHBoxLayout()
        
        self.prev_button = QPushButton("< Previous")
        self.prev_button.clicked.connect(self.previous_month)
        nav_layout.addWidget(self.prev_button)
        
        self.month_label = QLabel()
        self.month_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        nav_layout.addWidget(self.month_label)
        
        self.next_button = QPushButton("Next >")
        self.next_button.clicked.connect(self.next_month)
        nav_layout.addWidget(self.next_button)
        
        layout.addLayout(nav_layout)
        
        # Dashboard content area
        self.content_frame = QFrame()
        self.content_frame.setFrameStyle(QFrame.StyledPanel)
        self.content_layout = QVBoxLayout()
        self.content_frame.setLayout(self.content_layout)
        layout.addWidget(self.content_frame)
        
        self.setLayout(layout)
        self.update_month_label()
    
    def update_month_label(self):
        """Update the month label with current month/year."""
        month_name = datetime(self.current_year, self.current_month, 1).strftime("%B %Y")
        self.month_label.setText(month_name)
    
    def previous_month(self):
        """Navigate to previous month."""
        self.current_month -= 1
        if self.current_month < 1:
            self.current_month = 12
            self.current_year -= 1
        self.update_month_label()
        self.load_data()
        self.month_changed.emit(self.current_year, self.current_month)
    
    def next_month(self):
        """Navigate to next month."""
        self.current_month += 1
        if self.current_month > 12:
            self.current_month = 1
            self.current_year += 1
        self.update_month_label()
        self.load_data()
        self.month_changed.emit(self.current_year, self.current_month)
    
    def load_data(self):
        """Load and display data for current month."""
        # Clear existing content
        while self.content_layout.count():
            child = self.content_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        # Get transactions for current month
        transactions = self.data_store.get_transactions_by_month(self.current_year, self.current_month)
        
        # Calculate totals
        total_spent = sum(t.amount for t in transactions if t.amount > 0)
        total_refunds = sum(-t.amount for t in transactions if t.amount < 0)
        net_spent = total_spent - total_refunds
        
        # Category breakdown (refunds are stored as negative amounts)
        category_totals = defaultdict(float)
        for t in transactions:
            # Simply add the amount directly; refunds are already negative
            category_totals[t.category] += t.amount
        
        # Display totals
        totals_label = QLabel(f"Total Spent: ${total_spent:.2f} | Net Spent: ${net_spent:.2f}")
        totals_label.setStyleSheet("font-size: 14px;")
        self.content_layout.addWidget(totals_label)
        
        # Category breakdown
        if category_totals:
            breakdown_label = QLabel("Category Breakdown:")
            breakdown_label.setStyleSheet("font-size: 12px; font-weight: bold;")
            self.content_layout.addWidget(breakdown_label)
            
            # Text-based bar chart
            max_amount = max(category_totals.values()) if category_totals else 1
            for category, amount in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
                bar_width = int((amount / max_amount) * 20) if max_amount > 0 else 0
                bar = "█" * bar_width
                category_line = QLabel(f"{category}: ${amount:.2f} {bar}")
                category_line.setStyleSheet("font-family: monospace;")
                self.content_layout.addWidget(category_line)
        else:
            no_data_label = QLabel("No transactions for this month.")
            self.content_layout.addWidget(no_data_label)
        
        # Add spacer
        self.content_layout.addStretch()
    
    def refresh(self):
        """Refresh the dashboard display."""
        self.load_data()
