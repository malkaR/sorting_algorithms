from base import Sort


class BubbleSort(Sort):
    """Performs bubble sort on an input list"""
    def sort(self):
        for i in range(self.length-1, 0, -1):
            for index, item in enumerate(self.lst[:i]):
                if self.lst[index+1] < item:
                    self.swap(index, index+1)
        return self.lst

    def swap(self, index, index2):
        """Swaps two items with the given indices in the input list"""
        self.lst[index], self.lst[index2] = self.lst[index2], self.lst[index]
