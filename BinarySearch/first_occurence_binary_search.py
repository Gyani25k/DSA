class FindFirstOccurenceViaBinarySearch:

    def __init__(self, list):
        self.list = list

    def _first_occurence_calculation(self, target, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if self.list[mid] == target:
            if mid == 0 or self.list[mid - 1] != target:
                return mid
            else:
                return self._first_occurence_calculation(target, low, mid - 1)
        elif self.list[mid] > target:
            return self._first_occurence_calculation(target, low, mid - 1)
        else:
            return self._first_occurence_calculation(target, mid + 1, high)

    def search(self, target):
        return self._first_occurence_calculation(target, 0, len(self.list) - 1)

binary_search = FindFirstOccurenceViaBinarySearch([1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10])
# print(binary_search.search(1))  
# print(binary_search.search(2))  
# print(binary_search.search(3))  
