s=0
def game():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()

game_board=[["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]
s=0
game()

def check_game():
    if game_board[0][0]=="o" and game_board[0][1]=="o" and game_board[0][2]=="o":
        print("Player1 is the winner")
        s=1
    
    if game_board[1][0]=="o" and game_board[1][1]=="o" and game_board[1][2]=="o":
        print("Player1 is the winner")
        s=1

    if game_board[2][0]=="o" and game_board[2][1]=="o" and game_board[2][2]=="o":
        print("Player1 is the winner")
        s=1

    if game_board[0][0]=="o" and game_board[1][0]=="o" and game_board[2][0]=="o":
        print("Player1 is the winner")
        s=1

    if game_board[0][1]=="o" and game_board[1][1]=="o" and game_board[2][1]=="o":
        print("Player1 is the winner")
        s=1

    if game_board[0][2]=="o" and game_board[1][2]=="o" and game_board[2][2]=="o":
        print("Player1 is the winner")
        s=1
    
    if game_board[0][0]=="o" and game_board[1][1]=="o" and game_board[2][2]=="o":
        print("Player1 is the winner")
        s=1
    
    if game_board[0][2]=="o" and game_board[1][1]=="o" and game_board[2][0]=="o":
        print("Player1 is the winner")
        s=1

    if game_board[0][0]=="x" and game_board[0][1]=="x" and game_board[0][2]=="x":
        print("Player2 is the winner")
        s=1
    
    if game_board[1][0]=="x" and game_board[1][1]=="x" and game_board[1][2]=="x":
        print("Player2 is the winner")
        s=1

    if game_board[2][0]=="x" and game_board[2][1]=="x" and game_board[2][2]=="x":
        print("Player2 is the winner")
        s=1

    if game_board[0][0]=="x" and game_board[1][0]=="x" and game_board[2][0]=="x":
        print("Player2 is the winner")
        s=1

    if game_board[0][1]=="x" and game_board[1][1]=="x" and game_board[2][1]=="x":
        print("Player2 is the winner")
        s=1

    if game_board[0][2]=="x" and game_board[1][2]=="x" and game_board[2][2]=="x":
        print("Player2 is the winner")
        s=1
    
    if game_board[0][0]=="x" and game_board[1][1]=="x" and game_board[2][2]=="x":
        print("Player2 is the winner")
        s=1
    
    if game_board[0][2]=="x" and game_board[1][1]=="x" and game_board[2][0]=="x":
        print("Player2 is the winner")
        s=1

def tie():
    if game_board[0][0]!="-" and game_board[0][1]!="-" and game_board[0][2]!="-" and game_board[1][0]!="-" and game_board[1][1]!="-" and game_board[1][2]!="-" and game_board[2][0]!="-" and game_board[2][1]!="-" and game_board[2][2]!="-":
        print("No winner!")

while True:
#playe 1: (o)
    print("Player1: ")
    while True:
        row=int(input("Enter the row: "))
        cul=int(input("Enter the cell: "))
        if 0<=row<=2 and 0<=cul<=2:
            if game_board[cul][row]=="-":
                game_board[cul][row]= "o"
                game()
                check_game()
                break
            else:
                print("Choose another place please")
        else:
            print("Choose between 0-2")
    if s==1:
        break
    tie()
    

#player2: (x)
    print("Player2: ")
    while True:
        row=int(input("Enter the row: "))
        cul=int(input("Enter the cell: "))
        if 0<=row<=2 and 0<=cul<=2:
            if game_board[cul][row]=="-":
                game_board[cul][row]= "x"
                game()
                check_game()
                break
            else:
                print("Choose another place please")
        else:
            print("Choose between 0-2")

    if s==1:
        break
    tie()
    