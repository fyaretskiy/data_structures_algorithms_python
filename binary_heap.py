"""
heapq in python
-priority que algorithm
-smallest element is heap[0]
-pop return smallest item, min heap

"""

class Binheap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while i // 2 > 0: # first checks last item, when while loop statment ends, i looks in the middle
            if self.heap_list[i] < self.heap_list[i // 2]:
                temp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = temp
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_down(self, i):
        while (i * 2) <= self.current_size: # takes i=1
            mc = self.min_child(i) #
            if self.heap_list[i] > self.heap_list[mc]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]:
                self.heap_list[mc] = temp
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        ret_val = self.heap_list[1] # save first item
        self.heap_list[1] = self.heap_list[self.current_size]  # copy last item into first spot
        self.current_size -= 1 # change size
        self.heap_list.pop() # remove last item
        self.perc_down(1)
        return ret_val

