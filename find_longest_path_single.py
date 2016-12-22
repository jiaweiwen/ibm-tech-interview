"""This script aims at find the longest consecutive sequence starting from the 
top left conner of the 2-d grid.

To run this script in command: $python find_longest_path.py 
Sample input files: input_test.txt
"""

def LongestSequence(target_grid, row_idx, col_idx, cand_seq, final_seq):
    """
    This function finds the longest sequence on four different directions.

    Input:
        target_grid: the original input 2-d grid.
        row_idx: the row index of the current position.
        col_idx: the col index of the current position.
        cand_seq: the list of candidate sequence for the current search.
        final_seq: the list of candidate sequence with the longest length
            for the current search.

    Output:
        final_seq: the list of candidate sequence with the longest length
            for the current search.
    """

    # If the target_grid is an empty list or not.
    if len(target_grid) == 0 or len(target_grid[0]) == 0:
        return []

    row_len, col_len = len(target_grid), len(target_grid[0])

    # Append the current number to the candidate sequence.
    cand_seq.append(target_grid[row_idx][col_idx])

    # Determine if we have found a new consecutive path with longer length.
    if len(cand_seq) > len(final_seq):
        final_seq = list(cand_seq)

    # Search on the up direction.
    if row_idx > 0 and (target_grid[row_idx - 1][col_idx] == 
                        target_grid[row_idx][col_idx] + 1):
        final_seq = LongestSequence(target_grid, row_idx - 1, col_idx, 
                                    cand_seq, final_seq)
        cand_seq.pop(-1)
        
    # Search on the down direction.
    if row_idx < row_len - 1 and (target_grid[row_idx + 1][col_idx] == 
                                  target_grid[row_idx][col_idx] + 1):
        final_seq = LongestSequence(target_grid, row_idx + 1, col_idx, 
                                    cand_seq, final_seq)
        cand_seq.pop(-1)

    # Search on the left direction.
    if col_idx > 0 and (target_grid[row_idx][col_idx - 1] == 
                        target_grid[row_idx][col_idx] + 1):
        final_seq = LongestSequence(target_grid, row_idx, col_idx - 1, 
                                    cand_seq, final_seq)
        cand_seq.pop(-1)

    # Search on the right direction.
    if col_idx < col_len - 1 and (target_grid[row_idx][col_idx + 1] == 
                                  target_grid[row_idx][col_idx] + 1):
        final_seq = LongestSequence(target_grid, row_idx, col_idx + 1, 
                                    cand_seq, final_seq)
        cand_seq.pop(-1)

    return final_seq


def main():
    # Open the input file to get the 2-d grid.
    input_file = raw_input('Please enter the input file name: ')
    with open(input_file, "r") as file:
        target_grid = [[int(x) for x in line.split(',')] for line in file]

    # Determine the longest consecutive sequence of the target grid.
    final_seq = LongestSequence(target_grid, 0, 0, [], [])

    print 'The longest consecutive sequence is ', final_seq


if __name__ == '__main__':
    main()


