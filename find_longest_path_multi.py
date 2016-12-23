"""This script aims at find the longest consecutive sequence starting from the 
top left conner of the 2-d grid in a multi-threading manner.

To run this script in command: $python find_longest_path_multi.py 
Sample input files: input_test.txt
"""
import datetime
import threading
from threading import Thread

thread_lock = threading.Lock()
thread_num = 32
threads, final_seq = [], []

def LongestSequence(target_grid, row_idx, col_idx, cand_seq):
    """
    This function finds the longest sequence on four different directions with
    the help of threading.

    Input:
        target_grid: the original input 2-d grid.
        row_idx: the row index of the current position.
        col_idx: the col index of the current position.
        cand_seq: the list of candidate sequence for the current search.

    Output:
        None
    """
    global thread_lock, thread_num, threads, final_seq

    # If the target_grid is an empty list or not.
    if len(target_grid) == 0 or len(target_grid[0]) == 0:
        return []

    row_len, col_len = len(target_grid), len(target_grid[0])

    # Append the current number to the candidate sequence.
    cand_seq.append(target_grid[row_idx][col_idx])

    # Determine if we have found a new consecutive path with longer length. 
    thread_lock.acquire()
    if len(cand_seq) > len(final_seq): 
        del final_seq[:]
        for cand in cand_seq:
            final_seq.append(cand)
    thread_lock.release()
    
    # Search on the up direction.
    if row_idx > 0 and (target_grid[row_idx - 1][col_idx] == 
                        target_grid[row_idx][col_idx] + 1):
        if threading.activeCount() < thread_num:
            tmp_thread = Thread(target=LongestSequence, 
                args=(target_grid, row_idx - 1, col_idx, list(cand_seq)))
            tmp_thread.start()
            threads.append(tmp_thread)
        else:
            LongestSequence(target_grid, row_idx - 1, col_idx, list(cand_seq)) 
        
    # Search on the down direction.
    if row_idx < row_len - 1 and (target_grid[row_idx + 1][col_idx] == 
                                  target_grid[row_idx][col_idx] + 1):
        if threading.activeCount() < thread_num:
            tmp_thread = Thread(target=LongestSequence, 
                args=(target_grid, row_idx + 1, col_idx, list(cand_seq)))
            tmp_thread.start()
            threads.append(tmp_thread)
        else:
            LongestSequence(target_grid, row_idx + 1, col_idx, list(cand_seq)) 

    # Search on the left direction.
    if col_idx > 0 and (target_grid[row_idx][col_idx - 1] == 
                        target_grid[row_idx][col_idx] + 1):
        if threading.activeCount() < thread_num:
            tmp_thread = Thread(target=LongestSequence, 
                args=(target_grid, row_idx, col_idx - 1, list(cand_seq)))
            tmp_thread.start()
            threads.append(tmp_thread)
        else:
            LongestSequence(target_grid, row_idx, col_idx - 1, list(cand_seq)) 

    # Search on the right direction.
    if col_idx < col_len - 1 and (target_grid[row_idx][col_idx + 1] == 
                                  target_grid[row_idx][col_idx] + 1):
        if threading.activeCount() < thread_num:
            tmp_thread = Thread(target=LongestSequence, 
                args=(target_grid, row_idx, col_idx + 1, list(cand_seq)))
            tmp_thread.start()
            threads.append(tmp_thread)
        else:
            LongestSequence(target_grid, row_idx, col_idx + 1, list(cand_seq)) 

    return


def main():
    # Open the input file to get the 2-d grid.
    input_file = raw_input('Please enter the input file name: ')
    with open(input_file, "r") as file:
        target_grid = [[int(x) for x in line.split(',')] for line in file]

    start = datetime.datetime.now()

    # Determine the longest consecutive sequence of the target grid.
    LongestSequence(target_grid, 0, 0, [])
    
    for t in threads:
        t.join()

    end = datetime.datetime.now()

    print 'The longest consecutive sequence is ', final_seq
    print 'Execution time is %d ms' %int((end-start).total_seconds() * 1000000)


if __name__ == '__main__':
    main()

