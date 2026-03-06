class InsertionSort:

    def __init__(self,arr):
        self.arr = arr
    
    def sort(self):
        for i in range(1,len(self.arr)):
            x = self.arr[i]
            j = i-1

            while j>=0 and x < self.arr[j]:
                self.arr[j+1] = self.arr[j]
                j = j-1

            self.arr[j+1] = x
        
        return self.arr

list = [40,30,20,10]
insertion_sort = InsertionSort(list)
result = insertion_sort.sort()
print(result)