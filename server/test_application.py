import pytest

from application import TestMe

def test_take_five():
    server = TestMe()
    assert server.take_five() == 5

def test_port():
    server = TestMe()
    assert server.port == 8000
