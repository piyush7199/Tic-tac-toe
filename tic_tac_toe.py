import random as r

def print_gameboard(game_board):
    for i in game_board:
        for j in i:
            print(j,end=" ")
        print()

def set_pos(pos,game_board,user):
    sym = ""
    if(user == "player"):
        sym = "X"
    else:
        sym = "0"

    if(pos == 1):
        game_board[0][0] = sym
    elif(pos == 2):
        game_board[0][2] = sym
    elif(pos == 3):
        game_board[0][4] = sym
    elif(pos == 4):
        game_board[2][0] = sym
    elif(pos == 5):
        game_board[2][2] = sym
    elif(pos == 6):
        game_board[2][4] = sym
    elif(pos == 7):
        game_board[4][0] = sym
    elif(pos == 8):
        game_board[4][2] = sym
    else:
        game_board[4][4] = sym

def check_winner(pos,user):
    win = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    pos = sorted(pos)
    check = 3
    if(len(pos)>=3):
        for i in win:
            check = 3
            for j in i:
                if(j in pos):
                    check -= 1
                    if(check == 0):
                        return "Winner"

game_board = [[" ","|"," ","|"," "],["-","+","-","+","-"],[" ","|"," ","|"," "],["-","+","-","+","-"],[" ","|"," ","|"," "]]
print_gameboard(game_board)
cpl = []
ccl = []
while(True):
    player_pos = int(input("Enter the position: "))

    while((player_pos in cpl) or (player_pos in ccl)):
        player_pos = int(input("Enter the position: "))

    cpl.append(player_pos)
    set_pos(player_pos,game_board,"player")
    st = check_winner(cpl,"Player")

    if(st == "Winner"):
        print_gameboard(game_board)
        print("Player won the match")
        break

    if(len(cpl)==5):
        print_gameboard(game_board)
        print("It's Draw")
        break

    cpu_pos = r.randint(1,9)

    while((cpu_pos in ccl) or (cpu_pos in cpl)):
        cpu_pos = r.randint(1,9)

    ccl.append(cpu_pos)
    set_pos(cpu_pos,game_board,"cpu")
    st = check_winner(ccl,"Cpu")
    print_gameboard(game_board)

    if(st == "Winner"):
        print_gameboard(game_board)
        print("Computer won the match")
        break

    if(st=="Draw"):
        print(st)
        break
