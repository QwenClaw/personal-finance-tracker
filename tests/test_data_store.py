import unittest
from unittest.mock import MagicMock
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_store import DataStore
from transaction_model import Transaction
from PySide6.QtCore import QObject

class TestDataStore(unittest.TestCase):
    def setUp(self):
        DataStore._instance = None
        self.json_path = "test_transactions.json"
        self.data_store = DataStore(self.json_path)

    def tearDown(self):
        if os.path.exists(self.json_path):
            os.remove(self.json_path)

    def test_singleton_behavior(self):
        ds1 = DataStore(self.json_path)
        ds2 = DataStore(self.json_path)
        self.assertIs(ds1, ds2)

    def test_qobject_compatibility(self):
        # Verify DataStore is a QObject subclass
        self.assertTrue(issubclass(DataStore, QObject))
        # Verify instance is a QObject
        self.assertIsInstance(self.data_store, QObject)
        # Verify signal exists and is a Signal
        self.assertTrue(hasattr(self.data_store, 'data_changed'))

    def test_singleton_different_json_paths(self):
        # According to issue #80, singleton pattern should be enforced across different json_path values
        # This test verifies that the singleton pattern is maintained
        ds1 = DataStore("path1.json")
        ds2 = DataStore("path2.json")
        # Both should return the same instance (singleton pattern)
        self.assertIs(ds1, ds2)
        # The json_path should be the first one set
        self.assertEqual(ds1.json_path, "path1.json")

    def test_signal_emission(self):
        callback_mock = MagicMock()
        self.data_store.register_callback(callback_mock)
        transaction = Transaction(
            id="test1", amount=100.0, date="2023-01-01", category="Food", description="Test", is_refund=False
        )
        self.data_store.add_transaction(transaction)
        callback_mock.assert_called_once()

    def test_add_transaction(self):
        transaction = Transaction(
            id="test2", amount=200.0, date="2023-01-01", category="Rent", description="Test", is_refund=False
        )
        self.data_store.add_transaction(transaction)
        self.assertEqual(len(self.data_store.transactions), 1)

    def test_get_transactions_by_month(self):
        t1 = Transaction(id="t1", amount=100.0, date="2023-01-15", category="Food", description="Test", is_refund=False)
        t2 = Transaction(id="t2", amount=200.0, date="2023-02-20", category="Rent", description="Test", is_refund=False)
        self.data_store.add_transaction(t1)
        self.data_store.add_transaction(t2)
        jan = self.data_store.get_transactions_by_month(2023, 1)
        self.assertEqual(len(jan), 1)

    def test_save_and_load(self):
        t = Transaction(id="t3", amount=300.0, date="2023-03-10", category="Shopping", description="Test", is_refund=False)
        self.data_store.add_transaction(t)
        self.data_store.save()
        DataStore._instance = None
        new_store = DataStore(self.json_path)
        new_store.load()
        self.assertEqual(len(new_store.transactions), 1)

if __name__ == "__main__":
    unittest.main()
