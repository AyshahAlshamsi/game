# تعريف اللاعبين والمربعات
player1 = "X"
player2 = "O"
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# تعريف الدالة لطباعة اللوحة
def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# تعريف الدالة للتحقق من تحقق شروط الفوز
def check_win(player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False

# تعريف الدالة للعب اللعبة
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()
    current_player = player1
    game_over = False
    while not game_over:
        print(current_player + "'s turn.")
        position = int(input("Choose a position from 1-9: ")) - 1
        if board[position] == "-":
            board[position] = current_player
            print_board()
            if check_win(current_player):
                print(current_player + " wins!")
                game_over = True
            elif "-" not in board:
                print("Tie!")
                game_over = True
            else:
                if current_player == player1:
                    current_player = player2
                else:
                    current_player = player1

# بدء اللعبة
play_game()
# تعريف متغير لتخزين رسائل المحادثة
messages = []
# تعريف دالة لإرسال رسالة جديدة
def send_message(player, message):
    messages.append(player + ": " + message)