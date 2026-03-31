from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Transaction:
    """Represents a single financial transaction."""
    id: str
    amount: float
    date: str  # YYYY-MM-DD format
    category: str
    description: str
    is_refund: bool = False

    def __post_init__(self):
        # Validate amount
        if not isinstance(self.amount, (int, float)):
            raise ValueError("Amount must be a number")
        if self.amount == 0:
            raise ValueError("Amount cannot be zero")
        # Negative amounts are allowed for refunds (is_refund flag)
        
        # Validate date format
        try:
            datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
        
        # Validate category
        valid_categories = [
            "Food", "Rent", "Transport", "Entertainment", 
            "Shopping", "Health", "Bills", "Other"
        ]
        if self.category not in valid_categories:
            raise ValueError(f"Category must be one of: {', '.join(valid_categories)}")
