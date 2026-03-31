import json
import os
from typing import List, Optional, Callable
from transaction_model import Transaction
from PySide6.QtCore import QObject, Signal


class DataStore(QObject):
    """Singleton class to manage all data operations."""
    _instance = None
    data_changed = Signal()
    
    def __new__(cls, json_path: str = "transactions.json"):
        if cls._instance is None:
            # Use QObject.__new__ to ensure QObject compatibility
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, json_path: str = "transactions.json"):
        if self._initialized:
            return
        self._initialized = True
        self.json_path = json_path
        self.transactions = []
    
    def _emit_data_changed(self) -> None:
        """Emit data changed signal."""
        self.data_changed.emit()

    def register_callback(self, callback: Callable) -> None:
        """Register a callback to be called when data changes."""
        self.data_changed.connect(callback)
    
    def load(self) -> None:
        """Load transactions from JSON file."""
        if os.path.exists(self.json_path):
            try:
                with open(self.json_path, 'r') as f:
                    data = json.load(f)
                    self.transactions = [
                        Transaction(**t) for t in data.get("transactions", [])
                    ]
            except (json.JSONDecodeError, IOError):
                self.transactions = []
        else:
            self.transactions = []
    
    def save(self) -> None:
        """Save transactions to JSON file."""
        data = {
            "transactions": [
                {
                    "id": t.id,
                    "amount": t.amount,
                    "date": t.date,
                    "category": t.category,
                    "description": t.description,
                    "is_refund": t.is_refund
                } for t in self.transactions
            ]
        }
        with open(self.json_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_transaction(self, transaction: Transaction) -> None:
        """Add a transaction and auto-save."""
        self.transactions.append(transaction)
        self.save()
        self._emit_data_changed()
    
    def get_transactions_by_month(self, year: int, month: int) -> List[Transaction]:
        """Get all transactions for a specific month."""
        return [
            t for t in self.transactions
            if t.date.startswith(f"{year}-{month:02d}")
        ]
    
    def get_all_transactions(self) -> List[Transaction]:
        """Get all transactions."""
        return self.transactions.copy()
