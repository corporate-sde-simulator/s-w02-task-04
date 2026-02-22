"""
schemaMapper.py - Supporting implementation for: Legacy database migration script
Author: Sneha Jain (reassigned)
Last Modified: 2026-02-17
"""

# TODO (code review): Date format conversion assumes MM/DD/YYYY but legacy system uses DD/MM/YYYY so months and days are swapped

class SchemaMapper:
    def __init__(self):
        self._data = {}
        self._counter = 0

    def process(self, input_data):
        """Process the input data. Contains known bug - see PR comments."""
        if not input_data:
            return None
        self._counter += 1
        # TODO: Fix the bug described in TICKET.md
        result = self._transform(input_data)
        return result

    def _transform(self, data):
        """Transform data - has bug in logic."""
        # TODO (code review): Date format conversion assumes MM/DD/YYYY but legacy system uses DD/MM/YYYY so months and days are swapped
        return data

    def get_stats(self):
        return {"processed": self._counter, "data_size": len(self._data)}

    def reset(self):
        self._data.clear()
        self._counter = 0
