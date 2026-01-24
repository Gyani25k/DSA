
class BinaryRecursiveSearch:

    def __init__(self,list):
        self.list = list

    
    def _recursive_search(self,target,low,high):

        if low>high:
            return -1 

        mid = (low + high) //2

        if self.list[mid] == target:
            return mid
        elif self.list[mid] > target:
            return self._recursive_search(target,low, mid - 1)
        else:
            return self._recursive_search(target,mid+1, high)

    def search(self,target):
        return self._recursive_search(target,0,len(self.list)-1)


binary_search = BinaryRecursiveSearch([1,2,3,4,5,6,7,8,9,10])
print(binary_search.search(1))


binary_search = BinaryRecursiveSearch([1,2,3,4,5,6,7,8,9,10])
print(binary_search.search(5))


binary_search = BinaryRecursiveSearch([1,2,3,4,5,6,7,8,9,10])
print(binary_search.search(10))

binary_search = BinaryRecursiveSearch([1,2,3,4,5,6,7,8,9,10])
print(binary_search.search(11))
