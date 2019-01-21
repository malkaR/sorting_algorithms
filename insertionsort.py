from base import Sort


class InsertionSort(Sort):
    """Performs insertion sort on an input list"""
    def sort(self):
        if self.length <= 1:
            return self.lst
        for index in range(1, self.length):
            if self.lst[index] < self.lst[index-1]:
                self.insert(index)
        return self.lst

    def insert(self, index):
        """Insert the item at index in to a sorted position within the list,
        examining only the items within the list that are before index
        """
        item = self.lst.pop(index)
        # reverse the sorted part of the list, these include items
        # in the list that come before the index
        sorted_list_reversed = self.lst[index-1::-1]
        sorted_length = len(sorted_list_reversed)
        for i, list_item in enumerate(sorted_list_reversed):
            if item > list_item:
                self.lst.insert(sorted_length - i, item)
                return
        self.lst.insert(0, item)
