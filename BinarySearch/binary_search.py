class BinarySearch:
    def __init__(self,list):
        self.list = list
    

    def search(self,target):
        left = 0
        right = len(self.list)-1

        while left <= right:
            mid = (left + right)//2

            if self.list[mid] == target:
                return mid
            elif self.list[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return -1


binary_search = BinarySearch([1,2,3,4,5,6,7,8,9,10])
print(binary_search.search(5))


