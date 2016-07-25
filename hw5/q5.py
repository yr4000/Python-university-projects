##In order to test Q5 uncomment the following line
from matrix import * #matrix.py needs to be at the same directory

# a
def upside_down(im):
    n,m = im.dim()
    im2 = Matrix(n,m)
    for i in range(n):
        for k in range(m):
            im2.rows[i][k] = im.rows[n-i-1][m-k-1]
    return im2

# b
def reconstruct_image(m):
    puzzle_pieces = []
    for i in range(1,m**2+1): #create list of puzzle pieces
        puzzle_pieces.append(Matrix.load("puzzle\im{}.bitmap".format(i)))
    l,k = puzzle_pieces[0].dim()
    print(l,k)

    print("this is puzzle_pieces lengh: " , len(puzzle_pieces))
    puzzle_columns = [] #now constructing columns
    for i in range(m): 
        totem = puzzle_pieces[0]
        puzzle_pieces.remove(totem)
        for i in range(m-1):
            for piece in puzzle_pieces: 
                RN = len(totem.rows) #number of rows in totem
                if totem.rows[0] == piece.rows[l-1]: #checks the first row
                    totem.rows = totem.rows[1:]
                    piece.rows = piece.rows[:l-1]
                    totem.rows = piece.rows + totem.rows
                    #totem = piece
                    puzzle_pieces.remove(piece)
                    continue
                elif totem.rows[RN-1] == piece.rows[0]: #checks the last row
                    totem.rows = totem.rows[:RN -1]
                    piece.rows = piece.rows[1:]
                    totem.rows += piece.rows
                    puzzle_pieces.remove(piece)
        #print(totem.dim())
        #totem.display()
        totem.rows = totem.rows[1:len(totem.rows)-1]
        puzzle_columns.append(totem)

    print("this is puzzle_columns lengh: ", len(puzzle_columns))
    prize = puzzle_columns[0] #now to crack the secret! (construct the whole picture)
    puzzle_columns.remove(prize)
    RN = len(puzzle_columns[0].rows)
    CN = k
    print(prize.dim())
    for i in range(m-1):
        for column in puzzle_columns:
            CN = len(prize.rows[0]) #checks number of column in prize
            #print(RN,CN)
            prize_l_column = [prize.rows[i][0] for i in range(RN)]
            column_r_column = [column.rows[i][k-1] for i in range(RN)]
            
            if prize_l_column == column_r_column:
                #print("1")
                for i in range(RN):
                    prize.rows[i] = prize.rows[i][1:]
                    column.rows[i] = column.rows[i][:k-1]
                    prize.rows[i] = column.rows[i] + prize.rows[i]
                    #prize = column
                puzzle_columns.remove(column)
                continue

            #print("this is len " ,len(prize.rows[1]))
            #print(prize.dim())
            prize_r_column = [prize.rows[i][CN-1] for i in range(RN)]
            column_l_column = [column.rows[i][0] for i in range(RN)]
            
            if prize_r_column == column_l_column:
                #print("2")
                for i in range(RN):
                    prize.rows[i] = prize.rows[i][:CN-1]
                    column.rows[i] = column.rows[i][1:]
                    prize.rows[i] += column.rows[i]
                puzzle_columns.remove(column)
                
    #for i in range(m): #here we get rid of the extra pixels
     #   prize.rows.remove(prize.rows[i*l - i])
    #for i in range(m):
        #print((l-2)+i*l - i*2)
     #   prize.rows.remove(prize.rows[(l-2)+i*l - i*2])
    #print(len(prize.rows))
    #for RN in range(len(prize.rows)):
     #   for i in range(m):
      #      prize.rows[RN].remove(prize.rows[RN][i*k - i])
    #for RN in range(len(prize.rows)):
     #   for i in range(m):
      #      prize.rows[RN].remove(prize.rows[RN][k-2 + i*k - i*2])
    CN = len(prize.rows[0])
    for i in range(RN):
             prize.rows[i] = prize.rows[i][1:CN-1]
            
    print(prize.dim())
    #for i in range(len(puzzle_columns)):
     #   puzzle_columns[i].display()
    print("this is puzzle_pieces lengh at end: " , len(puzzle_pieces))
    print("this is puzzle_columns lengh at end: ", len(puzzle_columns))
    return prize

            
    
        
        
        
        
    
        
