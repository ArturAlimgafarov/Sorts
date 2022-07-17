from sorts import *
from random import randint as rand
import time

def main():
    sorts = [bubbleSort, countingSort, mergeSort, quickSort, heapSort, insertionSort, selectionSort, sorted]

    print('1. Bubble Sort')
    print('2. Counting Sort')
    print('3. Merge Sort')
    print('4. Quick Sort')
    print('5. Heap Sort')
    print('6. Insertion Sort')
    print('7. Selection Sort')
    print('8. Standard Python Sort Function')

    k: int = 0
    while True:
        k = int(input('Enter the corresponding sort number: '))
        if 0 < k < 9:
            break
        else:
            print('Wrong input')

    n: int = 0
    while True:
        n = int(input('Enter the count of array elements: '))
        if n > 0:
            break
        else:
            print('Wrong input')

    arr = [rand(-n, n) for _ in range(n)]
    print(f'Generated array of random numbers:\n{arr}')

    start = time.time()
    print(f'Sorted array:\n{sorts[k - 1](arr)}')
    end = time.time()
    print(f'Duration: {end - start} secs')

if __name__ == '__main__':
    main()