def bubbleSort(list):
    sortedList = list.copy()
    for _ in range(len(sortedList)):
        for j in range(len(sortedList) - 1):
            if sortedList[j] > sortedList[j + 1]:
                sortedList[j + 1], sortedList[j] = sortedList[j], sortedList[j + 1]
    return sortedList
def selectionSort(list):
    sortedList = list.copy()
    for i in range(len(sortedList) - 1):
        for j in range(i + 1, len(sortedList)):
            if sortedList[j] < sortedList[i]:
                sortedList[i], sortedList[j] = sortedList[j], sortedList[i]
    return sortedList
def insertionSort(list):
    sortedList = list.copy()
    for i in range(len(list) - 1):
        j = i + 1
        while j > 0 and sortedList[j] < sortedList[j - 1]:
            sortedList[j], sortedList[j - 1] = sortedList[j - 1], sortedList[j]
            j -= 1
    return sortedList
def quickSort(list):
    def partition(list, begin, end, pivot): # Hoare's method
        l, r = begin, end
        while l <= r:
            while list[l] < pivot: l += 1
            while list[r] > pivot: r -= 1
            if l <= r:
                list[l], list[r], l, r = list[r], list[l], l + 1, r - 1
        return l
    def qSort(list, begin, end):
        if (begin >= end):
            return
        pivot = list[(begin + end) // 2] # rand(begin, end) or begin or end
        index = partition(list, begin, end, pivot)
        qSort(list, begin, index - 1)
        qSort(list, index, end)
    sortedList = list.copy()
    qSort(sortedList, 0, len(list) - 1)
    return sortedList