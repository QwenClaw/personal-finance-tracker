import csv
import uuid
from typing import List, Dict, Set
from transaction_model import Transaction


class CSVImporter:
    """Utility for reading bank CSV files and converting to Transaction objects."""
    
    # Keyword to category mapping
    KEYWORD_CATEGORIES = {
        "Food": ["grocery", "restaurant", "cafe", "food", "supermarket", "market"],
        "Rent": ["rent", "lease", "apartment", "housing"],
        "Transport": ["uber", "lyft", "taxi", "gas", "fuel", "parking", "transit", "bus", "train"],
        "Entertainment": ["movie", "cinema", "netflix", "spotify", "game", "concert", "theater"],
        "Shopping": ["amazon", "store", "mall", "shop", "clothing", "retail"],
        "Health": ["pharmacy", "doctor", "hospital", "medical", "health", "gym", "fitness"],
        "Bills": ["utility", "electric", "water", "internet", "phone", "bill", "insurance"],
    }
    
    def __init__(self):
        self.seen_transactions: Set[str] = set()
    
    def _generate_id(self, date: str, amount: float, description: str) -> str:
        """Generate a unique ID based on transaction details for deduplication."""
        return f"{date}_{amount}_{description}"
    
    def _categorize(self, description: str) -> str:
        """Auto-categorize transaction based on keywords in description."""
        desc_lower = description.lower()
        for category, keywords in self.KEYWORD_CATEGORIES.items():
            for keyword in keywords:
                if keyword in desc_lower:
                    return category
        return "Other"
    
    def import_csv(self, file_path: str) -> List[Transaction]:
        """Read CSV file and return list of Transaction objects.
        
        Expected CSV format: amount, date, description
        - amount: positive number (refunds should be negative in CSV)
        - date: YYYY-MM-DD format
        - description: text description of transaction
        """
        transactions = []
        
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                
                # Check required columns
                if not all(col in reader.fieldnames for col in ['amount', 'date', 'description']):
                    raise ValueError("CSV must contain 'amount', 'date', and 'description' columns")
                
                for row in reader:
                    try:
                        # Parse amount (handle refunds as negative amounts)
                        amount = float(row['amount'])
                        is_refund = amount < 0
                        
                        # Parse date
                        date = row['date'].strip()
                        
                        # Get description
                        description = row['description'].strip()
                        
                        # Generate unique ID for deduplication
                        transaction_id = self._generate_id(date, amount, description)
                        
                        # Skip if already seen
                        if transaction_id in self.seen_transactions:
                            continue
                        
                        self.seen_transactions.add(transaction_id)
                        
                        # Auto-categorize
                        category = self._categorize(description)
                        
                        # Create transaction
                        transaction = Transaction(
                            id=str(uuid.uuid4()),
                            amount=abs(amount),  # Store positive amount
                            date=date,
                            category=category,
                            description=description,
                            is_refund=is_refund
                        )
                        
                        transactions.append(transaction)
                        
                    except (ValueError, KeyError) as e:
                        # Skip invalid rows but continue processing
                        print(f"Warning: Skipping invalid row: {row}. Error: {e}")
                        continue
        
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found: {file_path}")
        except Exception as e:
            raise Exception(f"Error reading CSV file: {e}")
        
        return transactions
