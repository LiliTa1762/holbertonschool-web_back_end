#!/usr/bin/env python3
"""
Testing utils module
"""


from parameterized import parameterized
import unittest
from utils import (access_nested_map)


class TestAccessNestedMap(unittest.TestCase):
    """Class to test nested map"""

    @parameterized.expand([
                         ({"a": 1}, ("a",), 1),
                         ({"a": {"b": 2}}, ("a",), {"b": 2}),
                         ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test_access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
                         ({}, ("a",), "a"),
                         ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception():
        """Parameterize a unit test"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
