
class FindFirstOccurenceViaBinarySearch:

    def __init__(self,list):
        self.list = list
    
    def _first_occurence_calculation(self,target,low,high):

        if low>high:
            return -1
        
        mid = (low+high) // 2

        if self.list[mid] == target:
            return mid

        if self.list[mid] > target:
            return self._first_occurence_calculation(target,mid + 1 ,high)

        
