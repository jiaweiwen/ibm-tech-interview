"""This script aims at find the longest consecutive sequence starting from the 
top left conner of the 2-d grid in a multi-threading manner.

To run this script in command: $python find_longest_path_multi.py 
Sample input files: input_test.txt
"""

import datetime
import threading
from threading import Thread

thread_num = 4
threads, max_step, thread_id = [], [0] * thread_num * 3, 0

def LongestSequence(target_grid, row_idx, col_idx, num_step):
    """
    This function finds the longest sequence on four different directions with
    the help of threading.

    Input:
        target_grid: the original input 2-d grid.
        row_idx: the row index of the current position.
        col_idx: the col index of the current position.
        num_step: the number of steps for the current search.

    Output:
        None
    """

    global thread_num, threads, thread_id, max_step

    # If the input is empty, return.
    if len(target_grid) == 0 or len(target_grid[0]) == 0:
        return

    # Calculate the bounds for rows and columns.
    row_len, col_len = len(target_grid), len(target_grid[0])

    # Determine if we have found a new consecutive path with longer length. 
    if num_step > max_step[thread_id - 1]: 
        max_step[thread_id - 1] = num_step

    # Generate the all the possible position in the next search.
    row_col_idx_list = [(row_idx - 1, col_idx), (row_idx + 1, col_idx),
                        (row_idx, col_idx - 1), (row_idx, col_idx + 1)]

    # Determine if we will do the next search for all the possibilities.
    for (new_row, new_col) in row_col_idx_list:
        if (new_row >= 0 and new_row < row_len and 
            new_col >= 0 and new_col < col_len and
            target_grid[new_row][new_col] == target_grid[row_idx][col_idx] + 1):
            
            # Implement multi-threading if the number of threads is less than
            # the predefined threshold for number of threads.
            if (threading.activeCount() < thread_num and 
                thread_id < len(max_step)):
                thread_id += 1
                tmp_thread = Thread(target=LongestSequence, 
                    args=(target_grid, new_row, new_col, num_step + 1))
                tmp_thread.start()
                threads.append(tmp_thread)
            else:
                LongestSequence(target_grid, new_row, new_col, num_step + 1) 

    return


def main():
    # Open the input file to get the 2-d grid.
    input_file = raw_input('Please enter the input file name: ')
    with open(input_file, "r") as file:
        target_grid = [[int(x) for x in line.split(',')] for line in file]

    # Record the starting time of the script.
    start = datetime.datetime.now()

    # Determine the longest consecutive sequence of the target grid.
    LongestSequence(target_grid, 0, 0, 0)
    
    for t in threads:
        t.join()

    # Record the ending time of the script.
    end = datetime.datetime.now()

    # Record the final sequence starting from the top left conner.
    if len(target_grid) == 0 or len(target_grid[0]) == 0:
        final_seq = []
    else:
        final_seq = range(target_grid[0][0], 
                          max(max_step) + target_grid[0][0] + 1)
    
    print 'The longest consecutive sequence is ', final_seq
    print 'Execution time is %d ms' %int((end-start).total_seconds() * 1000000)


if __name__ == '__main__':
    main()

