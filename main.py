import pandas as pd

class Piece:
    def __init__(self, is_white, type_of, location):
        self.is_white = is_white
        self.type_of = type_of
        self.location_of_piece = location
        
    def isWhite(self):
        return self.is_white
    
    def typeOf(self):
        return self.type_of
    
    def location(self):
        return self.location_of_piece
    
class Pawn(Piece):
    def moves(self):    
        x = self.location[0]
        y = self.location[1]

        ## needs check for frendlies
        if x == 1:
            df.iloc[x+2, y] = "M"
        if x < 7:
            df.iloc[x+1, y] = "M"    
            if y < 7:
                df.iloc[x+1, y+1] = "A"
            if y > 0:
                df.iloc[x+1, y-1] = "A"
                

class Rook(Piece):
    def moves(self):
        x = self.location[0]
        y = self.location[1]

        for i in range(0, x):
            df.iloc[i, y] = "M1"
        for i in range(x+1, 8):
            df.iloc[i, y] = "M2"
        for i in range(0, y):
            df.iloc[x, i] = "M3"
        for i in range(y+1, 8):
            df.iloc[x, i] = "M4"

                

## creates a pandas dataframe and fills the board with pieces in accordance with the FEN notation
def createDF():
    df = pd.DataFrame(columns=("a", "b", "c", "d", "e", "f", "g", "H"))
    # startFen = "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr"
    startFen = "RNBQKBNR/PPPPPPPP"
    numberString = "0123456789"

    for i in range(0, 8):
        df.loc[df.shape[0]] = ""

    count = 0
    for i in range(len(startFen)):
        if startFen[i] in numberString:
            count = count + int(startFen[i])
            for x in range(int(startFen[i])):
                df.iloc[(count//8), (count % 8)] = ""
        elif startFen[i] != "/":
            df.iloc[(count//8), (count % 8)] = startFen[i]
            count += 1

## displays the possible moves of the pawns, including attack possitions
def pawnPossibleMoves(capital, location):
    x = location[0]
    y = location[1]

    if capital == True:
        ## needs check for frendlies
        if y < 7:
            df.iloc[x+1, y+1] = "A"
        if y > 0:
            df.iloc[x+1, y-1] = "A"
        df.iloc[x+1, y] = "M"
        if x == 1:
            df.iloc[x+2, y] = "M"

## displays the possible moves of the rooks
def rookPossibleMoves(capital, location):
    x = location[0]
    y = location[1]

    for i in range(0, x):
        df.iloc[i, y] = "M1"
    for i in range(x+1, 8):
        df.iloc[i, y] = "M2"
    for i in range(0, y):
        df.iloc[x, i] = "M3"
    for i in range(y+1, 8):
        df.iloc[x, i] = "M4"

## displays the possible moves of the bischops
def bischopPossibleMoves(capital, location):
    x = location[0]
    y = location[1]

    for i in range(1, 9):
        if x+i < 8:
            if y+i < 8:
                df.iloc[x+i, y+i] = "B1"
            if y-i >= 0:
                df.iloc[x+i, y-i] = "B2"
        if x-i >= 0:
            if y+i < 8:
                df.iloc[x-i, y+i] = "B3"
            if y-i >= 0:
                df.iloc[x-i, y-i] = "B4"

## displays the possible moves of the queen
def queenPossibleMoves(capital, location):
    x = location[0]
    y = location[1]

    for i in range(1, 9):
        if x+i < 8:
            if y+i < 8:
                df.iloc[x+i, y+i] = "M"
            if y-i >= 0:
                df.iloc[x+i, y-i] = "M"
        if x-i >= 0:
            if y+i < 8:
                df.iloc[x-i, y+i] = "M"
            if y-i >= 0:
                df.iloc[x-i, y-i] = "M"

    for i in range(0, x):
        df.iloc[i, y] = "M"
    for i in range(x+1, 8):
        df.iloc[i, y] = "M"
    for i in range(0, y):
        df.iloc[x, i] = "M"
    for i in range(y+1, 8):
        df.iloc[x, i] = "M"

## displays the possible king moves
def kingPossibleMoves(capital, location):
    x = location[0]
    y = location[1]

    if x+1 < 8:
        if y+1 < 8:
            df.iloc[x+1, y+1] = "M"
        if y-1 >= 0:
            df.iloc[x+1, y-1] = "M"
    if x-1 >= 0:
        if y+1 < 8:
            df.iloc[x-1, y+1] = "M"
        if y-1 >= 0:
            df.iloc[x-1, y-1] = "M"

    if x+1 < 8:
        df.iloc[x+1, y] = "M"
    if x-1 >= 0:
        df.iloc[x-1, y] = "M"
    if y+1 < 8:
        df.iloc[x, y+1] = "M"
    if y-1 > 0:
        df.iloc[x, y-1] = "M"

## displays the possible knight moves
def knightPossibleMoves(capital, location):
    x = location[0]
    y = location[1]

    if x+2 < 8:
        if y+1 < 8:
            df.iloc[x+2, y+1] = "M"
        if y-1 >= 0:
            df.iloc[x+2, y-1] = "M"
    if x+1 < 8:
        if y+2 < 8:
            df.iloc[x+1, y+2] = "M"
        if y-2 >= 0:
            df.iloc[x+1, y-2] = "M"

    if x-2 >= 0:
        if y+1 < 8:
            df.iloc[x-2, y+1] = "M"
        if y-1 >= 0:
            df.iloc[x-2, y-1] = "M"
    if x-1 >= 0:
        if y+2 < 8:
            df.iloc[x-1, y+2] = "M"
        if y-2 >= 0:
            df.iloc[x-1, y-2] = "M"













