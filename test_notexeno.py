# test_notexeno.py
"""
Tests for NoteXeno module.
"""

import unittest
from notexeno import NoteXeno

class TestNoteXeno(unittest.TestCase):
    """Test cases for NoteXeno class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NoteXeno()
        self.assertIsInstance(instance, NoteXeno)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NoteXeno()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
