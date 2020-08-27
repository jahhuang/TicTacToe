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
    
def check_for_winner(board):
    if 

