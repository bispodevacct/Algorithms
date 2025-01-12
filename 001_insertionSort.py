def insertionSort(array):
    for i in range(1, len(array)):
        temporaryValue = array[i]

        j = i - 1

        while j >= 0 and array[j] > temporaryValue:
            array[j + 1] = array[j]

            j = j - 1
        
        array[j + 1] = temporaryValue