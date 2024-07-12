"""
File: Intervals.py

Description: Takes a set of intervals and collapses all of the overlapping intervals. Orders all of the 
             intervals in increasing order of the size of the intervals.

Student Name: Ricardo Medina

Student UT EID: rem3885

Course Name: CS 313E

Input: tuples_list is an unsorted list of tuples denoting intervals
Output: a list of merged tuples sorted by the lower number of the
        interval
"""
import sys

def merge_tuples (tuples_list):
    "This function collapses overlapping intervals"
    tuples_list.sort()

    new_list = []
    i = 0

    while i < len(tuples_list) - 1:
        # if the intervals overlap, replace it with the new interval
        if tuples_list[i][1] >= tuples_list[i + 1][0]:
            res = (min(tuples_list[i][0], tuples_list[i + 1][0]),
                   max(tuples_list[i][1], tuples_list[i + 1][1]))
            
            tuples_list[i] = res
            del tuples_list[i + 1]
        
        else:
            # base case
            new_list.append(tuples_list[i])
            i += 1

    if tuples_list[-1] not in new_list:
        new_list.append(tuples_list[-1])

    return new_list



def sort_by_interval_size (tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """

    # utilizes sort method key parameter to pass a function
    tuples_list.sort(key = find_interval_length)
    return tuples_list

def find_interval_length(item):
    """Helper function that gets the interval size between two values"""
    return abs(item[1] - item[0])



def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = []
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
