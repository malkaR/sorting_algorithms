import unittest

from bubblesort import BubbleSort
from insertionsort import InsertionSort
from mergesort import MergeSort
from selectionsort import SelectionSort


class SortingTestsBase:
    """
    Base class for sorting algorithm's test cases.
    Subclasses must specify the kls attribute and inherit
    from unittest.TestCase.
    """
    def get_error_message(self, msg):
        return msg.format(self.kls.__name__)

    def test_sort_reversed(self):
        test_input = [4, 3, 2, 1]
        expected_result = [1, 2, 3, 4]
        err_msg = self.get_error_message(
            'A reversed input list should be sorted after {0} runs')
        self.assertEqual(expected_result, self.kls(test_input).sort(), err_msg)

    def test_sort_sorted(self):
        test_input = [1, 2, 3, 4]
        expected_result = [1, 2, 3, 4]
        err_msg = self.get_error_message(
            'A sorted input list should remain sorted after {0} runs')
        self.assertEqual(expected_result, self.kls(test_input).sort(), err_msg)

    def test_sort_mixed(self):
        test_input = [4, 5, 2, 3, 9]
        expected_result = [2, 3, 4, 5, 9]
        err_msg = self.get_error_message(
            'A mixed input list should be sorted after {0} runs')
        self.assertEqual(expected_result, self.kls(test_input).sort(), err_msg)

    def test_sort_empty(self):
        test_input = []
        err_msg = self.get_error_message(
            'An empty input list should be empty after {0} runs')
        self.assertEqual(test_input, self.kls(test_input).sort(), err_msg)

    def test_sort_one_item(self):
        test_input = [3]
        expected_result = [3]
        err_msg = self.get_error_message(
            'A single item input list should be the same after {0} runs')
        self.assertEqual(expected_result, self.kls(test_input).sort(), err_msg)

    def test_sort_two_items(self):
        test_input = [3, 2]
        expected_result = [2, 3]
        err_msg = self.get_error_message(
            'A two item input list should be sorted after {0} runs')
        self.assertEqual(expected_result, self.kls(test_input).sort(), err_msg)

    def test_sort_duplicates(self):
        test_input = [2, 3, 2]
        expected_result = [2, 2, 3]
        err_msg = self.get_error_message(
            'An input list containing duplicates should '
            'be sorted after {0} runs')
        self.assertEqual(expected_result, self.kls(test_input).sort(), err_msg)


class BubbleSortTests(unittest.TestCase, SortingTestsBase):

    def setUp(self):
        self.kls = BubbleSort


class SelectionSortTests(unittest.TestCase, SortingTestsBase):

    def setUp(self):
        self.kls = SelectionSort


class InsertionSortTests(unittest.TestCase, SortingTestsBase):

    def setUp(self):
        self.kls = InsertionSort


class MergeSortTests(unittest.TestCase, SortingTestsBase):

    def setUp(self):
        self.kls = MergeSort


if __name__ == '__main__':
    unittest.main()
