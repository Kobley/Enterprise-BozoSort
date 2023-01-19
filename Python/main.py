# @author: Kobley#8008
# @purpose: shut up nerd
# @version: 0.0.1
# @disc: OOP style python enterprise implementation of big O of n(1) sorting algorithm, BozoSort™
# @TODO: encapsulate threading into multiprocessing pool to increase speed of algorithm from O(1) to O("faster than 1") (yes its a string it increases performance)

# chapter 1, imports ###############################################################################

# import the "Thread" object from package "threading"
from threading import Thread
# import package "numpy" as the more dev friendly term "np"
import numpy as np
# import the "time" method from package "time"
from time import time

# chapter 1, imports end ###############################################################################

# chapter 2, variables ###############################################################################

# container for storing the threads
tl_threads = []

# chapter 2, variables end ###############################################################################

# chapter 4, misc functions ###############################################################################

# function for creating lists of ints, size based on range object
# Example: createList(1000, range(100)) - creates a list of 1000 integers, values ranging from 1-100
def createList(length:int, rangeIn:range):
    if not isinstance(length,int):
        raise("length must be an integer - createList()")

    if not isinstance(rangeIn,range):
        raise("rangeIn must be a range object - createList()")

    return list(np.random.randint(low=rangeIn.start, high=rangeIn.stop, size=length))

# function for checking if a "list" object of numbers is sorted
def isSorted(arrIn:list):
    if not isinstance(arrIn,list):
        raise("arrIn must be a list - isSorted()")

    if all(arrIn[i] <= arrIn[i+1] for i in range(len(arrIn) - 1)):
        return True
    else:
        return False

# function for executing BozoSort™ within threads
def runBozoIter(listIn:list, verbose:bool):
    while not isSorted(listIn):
        np.random.shuffle(listIn)
        if verbose:
            print(listIn)

# chapter 4, misc functions end ##############################################################################

# chapter 5, main ##############################################################################

def main():
    # creates list variable
    i_listLength:int = 9
    r_listSizeObject:range = range(100)
    l_newList:list = createList(i_listLength, r_listSizeObject)
    
    # creates start_time variable
    f_start_time:float = time()

    # for loop 1
    verbose:bool = False
    for _ in range(256):
        t:Thread = Thread(target=runBozoIter, args=(l_newList,verbose,), daemon=False)
        tl_threads.append(t)
        t.start()

    # if the list is sorted (it will be instantly because of how good BozoSort™ is) close
    if isSorted(l_newList):
        # for loop 2
        for threadI in tl_threads:
            threadI.join()

        # a call to the print function, 
        # heres a tutorial to help with understanding how to utilize this function https://realpython.com/python-print/
        print(f"List sorted, took {time() - f_start_time}s\n{l_newList}")

# chapter 5, main end ##############################################################################

if __name__ == '__main__':
    main()