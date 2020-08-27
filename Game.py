#5 spaces, so X would be '  X  ' (2 spaces on either side)
board = ['     ' for _ in range(9)]
def print_board(array_board):
    print('     |     |     ')
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-----------------')
    print('     |     |     ')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----------------')
    print('     |     |     ')
    print(board[6] + '|' + board[7] + '|' + board[8])

def check_for_winner(b, mark):
    return ((b[0] == mark and b[1] == mark and b[2] == mark) 
    or (b[3] == mark and b[4] == mark and b[5] == mark) 
    or (b[6] == mark and b[7] == mark and b[8] == mark)
    or (b[0] == mark and b[3] == mark and b[6] == mark)
    or (b[1] == mark and b[4] == mark and b[7] == mark)
    or (b[2] == mark and b[5] == mark and b[8] == mark)
    or (b[0] == mark and b[4] == mark and b[8] == mark)
    or (b[2] == mark and b[4] == mark and b[6] == mark))

#Don't need to check for empty space, since there are nine spaces only?

