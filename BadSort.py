import random
import time

def fast_sort(lst):
    while not (all(lst[i] <= lst[i+1] for i in range(len(lst)-1))):
        lst = random.sample(lst, len(lst))
    return lst


for num in range(1,12):
    timelist = []
    for it in range(1,50):

        # Generate a random list
        randomlist = []
        for i in range(1,num):
            n = random.randint(1,num)
            randomlist.append(n)

        #Run the sort algorithm on it
        start_time = time.time()
        new_list = fast_sort(randomlist)
        end_time = time.time()
        timelist.append(end_time - start_time)
        
    aver = str(sum(timelist)/len(timelist))
    print("--- %s seconds average for %d ---" % (aver, num))
