from base import Sort


class MergeSort(Sort):
    """Performs merge sort on an input list"""
    def sort(self):
        return self.merge_sort(self.lst)

    @staticmethod
    def merge_sort(lst):
        """
        Sort a list by splitting it in half,
        and combining the sorted results
        """
        length = len(lst)
        if length == 0:
            return []
        if length == 1:
            return MergeSort.merge(lst, [])
        half_length = length // 2
        return MergeSort.merge(
            MergeSort.merge_sort(lst[:half_length]),
            MergeSort.merge_sort(lst[half_length:]))

    @staticmethod
    def merge(lst1, lst2):
        """
        Merge the two sorted input lists,
        while maintaining a sorted order.
        """
        new_list = []

        while lst1:
            if lst2 and lst2[0] < lst1[0]:
                new_list.append(lst2.pop(0))
            else:
                new_list.append(lst1.pop(0))

        if lst2:
            new_list += lst2
        elif lst1:
            new_list += lst1

        return new_list
