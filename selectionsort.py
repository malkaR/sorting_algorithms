from base import Sort


class SelectionSort(Sort):
    """Performs selection sort on an input list"""
    def sort(self):
        new_list = []

        for _ in range(self.length):
            min_item = min(self.lst)
            new_list.append(min_item)
            self.lst.pop(self.lst.index(min_item))

        return new_list
