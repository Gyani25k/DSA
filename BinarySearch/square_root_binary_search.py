

class SquareRootFinderByBinarySearch:

    def square_root(self, target):
        if target < 2:
            return target

        low = 0
        high = target

        while low <= high:
            mid = (low + high) // 2
            mid_sq = mid * mid

            if mid_sq == target:
                return mid
            elif mid_sq > target:
                high = mid - 1
            else:
                low = mid + 1

        return high  


finder = SquareRootFinderByBinarySearch()
print(finder.square_root(16))  # Output: 4
print(finder.square_root(17))  # Output: 4
print(finder.square_root(1))   # Output: 1
print(finder.square_root(0))   # Output: 0