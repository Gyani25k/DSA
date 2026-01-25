class LastOccurenceBinarySearch:
    def __init__(self,list):
        self.list = list
    
    def _last_occurence_binary_search(self,target,low,high):
        
        if low>high:
            return -1

        mid = (low + high) // 2

        if self.list[mid] == target:
            if mid == 0 or self.list[mid] != self.list[mid+1]:
                return mid
            else:
                return self._last_occurence_binary_search(target,mid +1,high)
        elif self.list[mid] > target:
            return self._last_occurence_binary_search(target,low,mid -1)

        else:
            return self._last_occurence_binary_search(target,mid+1,high)


    def search(self,target):
        return self._last_occurence_binary_search(target,0,len(self.list)-1)

binary_search = LastOccurenceBinarySearch([1,1, 2, 2, 3, 3, 4, 5, 6, 7,7,7,7,7, 8, 9, 10])
# print(binary_search.search(1))  
# print(binary_search.search(2))  
# print(binary_search.search(3))
# print(binary_search.search(7))
# print(binary_search.search(11))    