"""
Module helloworld.py: Contains function to print "Hello world of Python".
"""

from mockito import mock, verify
import unittest

from helloworld import helloworld


class HelloWorldTest(unittest.TestCase):
    """
    Test case for the helloworld function.
    """

    def test_should_issue_hello_world_message(self):
        """
        Test if helloworld function writes "Hello world of Python" to the output stream.
        """
        out = mock()

        helloworld(out)

        verify(out).write("Hello world of Python\n")
