class BubbleSort:
    def __init__(self, list):
        self.list = list

    def sort(self):
        n = len(self.list)
        for i in range(n-1):
            for j in range(n-i-1):
                if self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]
        return self.list

list = [1, 0, 3, 2]
bubble_sort = BubbleSort(list=list)
print(bubble_sort.sort())