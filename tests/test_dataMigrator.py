"""Tests for Legacy database migration script."""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from dataMigrator import DataMigrator
from schemaMapper import SchemaMapper

class TestMain:
    def test_basic(self):
        obj = DataMigrator()
        assert obj.process({"key": "val"}) is not None
    def test_empty(self):
        obj = DataMigrator()
        assert obj.process(None) is None
    def test_stats(self):
        obj = DataMigrator()
        obj.process({"x": 1})
        assert obj.get_stats()["processed"] == 1

class TestSupport:
    def test_basic(self):
        obj = SchemaMapper()
        assert obj.process({"key": "val"}) is not None

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
