#!/usr/bin/env python3
import sys, os

sys.path.insert(0, os.path.dirname(__file__))
import unittest
import tests.test_list_packages

suite = unittest.TestLoader().loadTestsFromModule(tests.test_list_packages)
unittest.TextTestRunner(verbosity=2).run(suite)
