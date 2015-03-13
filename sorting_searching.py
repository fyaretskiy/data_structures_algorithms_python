alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Sequential Search O(n)


def sequential_search(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


# Ordered Sequential Search O(n)


def ordered_sequential_search(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += pos

    return found


# Binary Search

def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) / 2  # python 3 // is integer div, and / float div. python 2 / is integer div
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


# The Bubble Sort O(n^2)


def bubble_sort(alist):
    for passnum in range(len(alist) - 1, 0, -1):  # range(start, stop[, step])
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


# print range(10, 0, -1)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# The Selection Sort


def selection_sort(alist):
    for fill_slot in range(len(alist) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if alist[location] > alist[position_of_max]:
                position_of_max = location

        temp = alist[fill_slot]
        alist[fill_slot] = alist[position_of_max]
        alist[position_of_max] = temp


# The Insertion Sort


def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = current_value


# The Shell Sort

def shell_sort(alist):
    sublist_count = len(alist) / 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist, start_position, sublist_count)

        print "After increments of size", sublist_count, "The list is", alist
        sublist_count /= 2


def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i

        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = current_value


# The Merge Sort

def merge_sort(alist):
    print "Splitting: ", alist
    if len(alist) > 1:
        mid = len(alist) / 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[i]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1
        print "Merging ", alist


# The Quick Sort


def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist)-1)


def quick_sort_helper(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)
        quick_sort_helper(alist, first, split_point-1)
        quick_sort_helper(alist, split_point+1, last)


def partition(alist, first, last):
    pivot_value = alist[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        while left_mark <= right_mark and alist[left_mark] <= pivot_value:
            left_mark += 1

        while alist[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True

        else:
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp

    temp = alist[first]
    alist[first] = alist[right_mark]
    alist[right_mark] = temp

    return right_mark


