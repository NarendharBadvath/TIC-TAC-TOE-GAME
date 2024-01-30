import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if is_winner(board, 'O'):
        return -1
    elif is_winner(board, 'X'):
        return 1
    elif is_board_full(board):
        return 0

    empty_cells = get_empty_cells(board)

    if maximizing_player:
        max_eval = float('-inf')
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'X'
            eval = minimax(board, depth + 1, False)
            board[cell[0]][cell[1]] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'O'
            eval = minimax(board, depth + 1, True)
            board[cell[0]][cell[1]] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    empty_cells = get_empty_cells(board)
    best_score = float('-inf')
    best_move = empty_cells[0]

    for cell in empty_cells:
        board[cell[0]][cell[1]] = 'X'
        score = minimax(board, 0, False)
        board[cell[0]][cell[1]] = ' '

        if score > best_score:
            best_score = score
            best_move = cell

    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'O'

    while not is_winner(board, 'O') and not is_winner(board, 'X') and not is_board_full(board):
        print_board(board)

        if player == 'O':
            row, col = map(int, input("Enter your move (row and column, separated by space): ").split())
            if board[row][col] != ' ':
                print("Cell already taken. Try again.")
                continue
        else:
            print("AI is making a move...")
            row, col = best_move(board)

        board[row][col] = player
        player = 'X' if player == 'O' else 'O'

    print_board(board)

    if is_winner(board, 'O'):
        print("You win!")
    elif is_winner(board, 'X'):
        print("AI wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()