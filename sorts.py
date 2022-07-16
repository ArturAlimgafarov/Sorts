def bubbleSort(list):
    sortedList = list.copy()
    for _ in range(len(sortedList)):
        for j in range(len(sortedList) - 1):
            if sortedList[j] > sortedList[j + 1]:
                sortedList[j + 1], sortedList[j] = sortedList[j], sortedList[j + 1]
    return sortedList