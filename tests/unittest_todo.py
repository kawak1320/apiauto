"""
(c) Copyright Jalasoft. 2023

projects.py
    configuration of logger file
"""
import unittest


class TestProject(unittest.TestCase):
    """
    Class for projects endpoint
    """

    # fixture
    def setUp(self):
        """
        Test setUp project
        :return:
        """
        print("Setup")

    def test_one(self):
        """
        Test test_one project
        :return:
        """
        print("test one")

    def test_two(self):
        """
        Test test_two project
        :return:
        """
        print("test two")

    def test_three(self):
        """
        Test test_three project
        :return:
        """
        print("test three")

    # fixture
    def tearDown(self):
        """
        Test tearDown project
        :return:
        """
        print("tearDown")
