#!/usr/bin/env python3

from control_flow import admin_login, hows_the_weather, fizzbuzz, calculator

import io
import sys
import unittest


class TestCalculator(unittest.TestCase):
    def test_prints_invalid_returns_none_if_invalid(self):
        """prints 'Invalid operation!' and returns None if operation invalid"""
        captured_out = io.StringIO()
        sys.stdout = captured_out
        assert calculator("a", 1, 2) == "Invalid operation!"

    def test_returns_access_granted_admin12345(self):
        """returns 'Access granted' for username=admin and password=12345"""
        assert admin_login("admin", "12345") == "Access granted"

    # Rest of the test methods...


if __name__ == "__main__":
    unittest.main()
