def linearSearch(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1