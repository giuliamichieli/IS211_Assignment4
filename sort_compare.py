import time, random

def insertion_sort(alist):
    start = time.process_time_ns()/1000000
    for i in range(1, len(alist)):
        key = alist[i]
        j = i-1
        while j >=0 and key < alist[j] :
            alist[j+1] = alist[j] 
            j -= 1
        alist[j+1] = key
    total_time = round(time.process_time_ns()/1000000 - start,2)
    return total_time # total_time in seconds

def shell_sort(alist):
    start = time.process_time_ns()/1000000
    n = len(alist)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = alist[i]
            j = i
            while j >= interval and alist[j - interval] > temp:
                alist[j] = alist[j - interval]
                j -= interval

            alist[j] = temp
        interval //= 2
    total_time = round(time.process_time_ns()/1000000 - start,2)
    return total_time # total_time in seconds

def python_sort(alist):
    start = time.process_time_ns()/1000000
    sorted(alist)
    total_time = round(time.process_time_ns()/1000000 - start,2)
    return total_time # total_time in seconds
	

if __name__ == "__main__":

    for size in [500, 1000, 10000]:
        insert_t = 0.0
        shell_t = 0.0
        python_t = 0.0
        for i in range(100):
            test_list = [random.randint(1,size) for j in range(size)]

            took = insertion_sort(test_list)
            insert_t += took

            took = shell_sort(test_list)
            shell_t += took

            took = python_sort(test_list)
            python_t += took

        insert_avg = insert_t /100
        shell_avg = shell_t / 100
        python_avg = python_t / 100

        print ("\nFor a list of %d elements :" % size)
        print ("Insertion Sort took %10.7f seconds to run, on average" % insert_avg)
        print ("Shell Sort took %10.7f seconds to run, on average" % shell_avg)
        print ("Python Sort took %10.7f seconds to run, on average" % python_avg)