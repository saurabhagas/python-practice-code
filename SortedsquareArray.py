
def sortedSquaredArray(array):
    squared_array = [0 for _ in array]
    left = 0
    right = len(array) - 1

    for i in reversed(range(len(array))):
        if abs(array[left]) > abs(array[right]):
            squared_array[i] = array[left] ** 2
            left += 1
        else:
            squared_array[i] = array[right] ** 2
            right -= 1

    return squared_array


