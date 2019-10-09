from models.Couch import Couch
import time

def merge(A, B):
    global merge_swap_count
    global merge_compare_count
    i1 = i2 = 0
    out = []
    while i1 < len(A) and i2 < len(B):
        merge_compare_count += 1
        if A[i1].length <= B[i2].length:
            out.append(A[i1])
            i1 += 1
            merge_swap_count += 1
        else:
            out.append(B[i2])
            i2 += 1
            merge_swap_count += 1
    out += A[i1:] + B[i2:]
    merge_swap_count += len(A)-i1 + len(B)-i2
    return out

def mergeSort(A):
    if len(A) <= 1:
        return A
    mid = int(len(A) / 2)
    return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))


def selectionSort(A):
    global selection_swap_count
    global selection_compare_count
    for i in range(len(A)):
        min_i = i
        for j in range(i+1, len(A)):
            selection_compare_count += 1
            if A[j].width >= A[min_i].width:
                min_i = j
        A[i], A[min_i] = A[min_i], A[i]
        selection_swap_count += 1

arr = []

with open('input.txt', 'r') as input:
    fields = input.read().split(',')
    i = 0
    width = 0
    length = 0
    for field in fields:
        i += 1
        if(i % 4 == 1):
            width = int(field)
        if(i % 4 == 2):
            length = int(field)
        if(i % 4 == 3):
            color = str(field)
        if(i % 4 == 0):
            arr.append(Couch(width, length, color, field))

selection_begin = time.time()
selection_compare_count = 0
selection_swap_count = 0
selectionSort(arr)
selection_finish = time.time()

with open('output.txt', 'a+') as output:
    output.write('SELECTION SORT\n')
    output.write('Time: ' + str(selection_finish-selection_begin) + '\n')
    output.write('Compares: ' + str(selection_compare_count) + '\n')
    output.write('Swaps: ' + str(selection_swap_count) + '\n')
    output.write('Elements:\n')
    for a in arr:
        output.write(str(a))
        if a.brand.find('\n') == -1:
            output.write('\n')

merge_begin = time.time()
merge_compare_count = 0
merge_swap_count = 0
arr = mergeSort(arr)
merge_finish = time.time()

with open('output.txt', 'a+') as output:
    output.write('MERGE SORT\n')
    output.write('Time: ' + str(merge_finish - merge_begin) + '\n')
    output.write('Compares: ' + str(merge_compare_count) + '\n')
    output.write('Swaps: ' + str(merge_swap_count) + '\n')
    output.write('Elements:\n')
    for a in arr:
        output.write(str(a))
        if a.brand.find('\n') == -1:
            output.write('\n')
