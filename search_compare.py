import time, random

def sequential_search(alist, item):
    start = time.process_time_ns()/1000000
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    total_time = round(time.process_time_ns()/1000000 - start,2)
    return found, total_time # total_time in seconds


def orderedSequentialSearch(alist, item):
    start = time.process_time_ns()/1000000
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
	            pos = pos+1
    total_time = round(time.process_time_ns()/1000000 - start,2)
    return found, total_time # total_time in seconds

def binary_search_iterative(alist, item):
    start = time.process_time_ns()/1000000
    low = 0
    high = len(alist) - 1
    mid = 0
    found = False
    while low <= high:
        mid = low + (high - low) // 2
        if alist[mid] == item:
            found = True
            break
        elif alist[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    total_time = round(time.process_time_ns()/1000000 - start,2)
    return found, total_time # total_time in seconds

def binary_search_recursive(alist, item):
    start = time.process_time_ns()/1000000
    found = binary_search_recursive_inner(alist, item)
    total_time = round(time.process_time_ns()/1000000 - start,2)
    return found, total_time # total_time in seconds


def binary_search_recursive_inner(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
	            return binary_search_recursive_inner(alist[:midpoint],item)
            else:
                return binary_search_recursive_inner(alist[midpoint+1:],item)
	

if __name__ == "__main__":

    for size in [500, 1000, 10000]:
        seq_t = 0.0
        ordseq_t = 0.0
        biniter_t = 0.0
        binrec_t = 0.0
        for i in range(100):
            test_list = sorted([random.randint(1,size) for j in range(size)])

            found, took = sequential_search(test_list, -1)
            seq_t += took

            found, took = orderedSequentialSearch(test_list, -1)
            ordseq_t += took

            found, took = binary_search_iterative(test_list, -1)
            biniter_t += took

            found, took = binary_search_recursive(test_list, -1)
            binrec_t += took

        seq_avg = seq_t / 100
        ordseq_avg = ordseq_t /100
        biniter_avg = biniter_t / 100
        binrec_avg = binrec_t / 100

        print ("\nFor a list of %d elements:" % size)
        print ("Sequential Search took %10.7f seconds to run, on average" % seq_avg)
        print ("Ordered Sequential Search took %10.7f seconds to run, on average" % ordseq_avg)
        print ("Binary Iterative Search took %10.7f seconds to run, on average" % biniter_avg)
        print ("Binary Recursive Search took %10.7f seconds to run, on average" % binrec_avg)