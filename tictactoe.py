row0 = [0,0,0]
row1 = [0,0,0]
row2 = [0,0,0]
board = [row0,row1,row2]
print board[0]
print board[1]
print board[2]
win = False
turn= [0]

def pick(list, board, row0, row1, row2):
    if turn[0]%2 == 0:
        player1 = True
    else:
        player1 = False
    
    row_pick = input("pick a row (1 - 3):")
    col_pick = input("pick a column(1 - 3):")
    sel_row = board[row_pick -1]
    sel_loc = sel_row[col_pick - 1]

    if sel_loc == 0:
        if player1 == True:
            board[row_pick -1][col_pick -1] = "X"
        elif player1 == False:
            board[row_pick -1][col_pick -1] = "O"
    elif sel_loc != 0 :
        print "That spot has already been taken"
        turn[0] -=1
        
    turn[0] +=1 
    
    print board[0]
    print board[1]
    print board[2]

def win_cond(win,row0,row1,row2):
    for i in range(0,3):
        if row0[i] == row1[i] == row2[i] and row0[i] != 0:
            print row0[0] + " WINS!"
            return True
    if row0[0] == row0[1] == row0[2] and row0[0] != 0:
        print row0[0] + " WINS!"
        return True
    if row1[0] == row1[1] == row1[2] and row1[0] != 0:
        print row1[0] + " WINS!"
        return True
    if row2[0] == row2[1] == row2[2] and row2[0] != 0:
        print row2[0] + " WINS!"
        return True
    if row0[0] == row1[1] == row2[2] and row0[0] != 0:
        print row0[0] + " WINS!"
        return True
    if row2[0] == row1[1] == row0[2] and row2[0] != 0:
        print row2[0] + " WINS!"
        return True
    haszero = [0,0,0]
    for i in range(0,3):
        if row0[i] == 0 or row1[i] == 0 or row2[i] ==0:
            haszero[i] = True
        else:
            haszero[i] = False
    print haszero
    if haszero[0] == haszero[1] == haszero[2] == False:
        print "TIE GAME!"
        return True
        
    return False
    

while win == False:
    pick(turn, board, row0, row1, row2)
    win = win_cond(win,row0,row1,row2)
    

    

