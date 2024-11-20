# Tic-Tac-Toe Game
def display_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2],  # First row
        [3, 4, 5],  # Second row
        [6, 7, 8],  # Third row
        [0, 3, 6],  # First column
        [1, 4, 7],  # Second column
        [2, 5, 8],  # Third column
        [0, 4, 8],  # Diagonal from top-left to bottom-right
        [2, 4, 6]   # Diagonal from top-right to bottom-left
    ]
    
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    return all(spot != " " for spot in board)

def play_game():
    board = [" " for _ in range(9)] 
    current_player = "X" 
    
    print("Welcome to Tic-Tac-Toe!")
    display_board(board)
    
    while True:
        move = -1
        while move < 0 or move > 8 or board[move] != " ":
            try:
                move = int(input(f"Player {current_player}, choose a position (0-8): "))
            except ValueError:
                print("Invalid input! Please choose a number between 0 and 8.")
        
        board[move] = current_player
        display_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        
        if is_board_full(board):
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
