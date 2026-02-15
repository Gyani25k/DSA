class SelectionSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n-1):
            mid_index = i
            for j in range(i+1, n):
                if self.arr[j] < self.arr[mid_index]:
                    mid_index = j
            self.arr[mid_index], self.arr[i] = self.arr[i], self.arr[mid_index]
        return self.arr

list = [1, 0, 3, 2]
selection_sort = SelectionSort(arr=list)
print(selection_sort.sort())
