import pytest
from app.tools import calculate
def test_calculate_order(): assert calculate("2 + 3 * 4")==14
def test_calculate_parentheses(): assert calculate("(10 - 4) / 2")==3
def test_reject_code():
    with pytest.raises(ValueError): calculate("__import__('os').system('whoami')")
