from first_occurence_binary_search import FindFirstOccurenceViaBinarySearch
from last_occurence_binary_search import LastOccurenceBinarySearch

class CountOccurenceOfBNunmbers:

    def __init__(self,list):
        self.list = list
        self.first_occurence_calculation = FindFirstOccurenceViaBinarySearch(self.list)
        self.last_occurence_calculation = LastOccurenceBinarySearch(self.list)

    def count(self,target):
        first_index = self.first_occurence_calculation.search(target)
        last_index = self.last_occurence_calculation.search(target)
        count = (last_index - first_index) + 1
        return count


binary_search = CountOccurenceOfBNunmbers([1,1, 2, 2, 3, 3, 4, 5, 6, 7,7,7,7,7, 8, 9, 10])
print(binary_search.count(7)) 