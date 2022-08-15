from site import venv
import pandas as pd

## creates a pandas dataframe and fills the board with pieces in accordance with the FEN notation
df = pd.DataFrame(index=range(8), columns=range(8))

## this function stores a lot of starting positions which makes it easy to toggle between them


def beginPositions():
    ## starting positions for a normal start
    startFen = "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr"

    ## starting positions for white only
    # startFen = "RNBQKBNR/PPPPPPPP"

    ## starting position without pawns
    #startFen = "RNBQKBNR/8/8/8/8/8/8/rnbqkbnr"

    ## custom starting position
    # startFen = "RNBQKBNR/8/8/8/3p4/8/8/rnbqkbnr"
    # startFen = "8/P2P2Pp/1Kp5/p"

    numberString = "0123456789"

    for row in range(0, 8):
        for column in range(0, 8):
            df.iloc[row, column] = 0

    count = 0
    for i in range(len(startFen)):
        if startFen[i] in numberString:
            count = count + int(startFen[i])
        elif startFen[i] != "/":
            df.iloc[(count//8), (count % 8)] = startFen[i]
            count += 1


beginPositions()


def straight(location, is_white, singular_step=False):
    horizontalArray = horizontal(location, is_white)
    verticalArray = vertical(location, is_white)

    if singular_step == True:
        x = []
        y = []
        for i in range(-1, 1):
            x[i+1] = horizontalArray[(location[0]+i)]
            y[i+1] = verticalArray[(location[0]+i)]
            return x, y
    else:
        return horizontalArray, verticalArray


def diagonal(location, is_white, singular_step=False):
    leftTop = []
    rightTop = []
    row, column = location

    pieceCounter = 0
    for i in range(1, row+1):
        if column-i >= 0:
            if pieceCounter == 0:
                if occupied([row-i, column-i])[0] == False:
                    leftTop.insert(0, "M")
                elif occupied([row-i, column-i])[1] != is_white:
                    leftTop.insert(0, "A")
                    pieceCounter = 1
                else:
                    leftTop.insert(0, "Same")
                    pieceCounter = 2
            elif pieceCounter == 1:
                if occupied([row-i, column-i])[0] == False:
                    leftTop.insert(0, "P")
                elif occupied([row-i, column-i])[1] != is_white:
                    leftTop.insert(0, "P")
                    pieceCounter = 2
                else:
                    leftTop.insert(0, "X")
                    pieceCounter = 2
            else:
                leftTop.insert(0, "X")

    pieceCounter = 0
    leftTop.append("location")

    for i in range(1, 8-row):
        if column+i < 8:
            if pieceCounter == 0:
                if occupied([row+i, column+i])[0] == False:
                    leftTop.append("M")
                elif occupied([row+i, column+i])[1] != is_white:
                    leftTop.append("A")
                    pieceCounter = 1
                else:
                    leftTop.append("Same")
                    pieceCounter = 2
            elif pieceCounter == 1:
                if occupied([row-i, column-i])[0] == False:
                    leftTop.append("P")
                elif occupied([row-i, column-i])[1] != is_white:
                    leftTop.append("P")
                    pieceCounter = 2
                else:
                    leftTop.append("X")
                    pieceCounter = 2
            else:
                leftTop.append("X")

    pieceCounter = 0
    for i in range(1, row+1):
        if column+i < 8:
            if pieceCounter == 0:
                if occupied([row-i, column+i])[0] == False:
                    rightTop.insert(0, "M")
                elif occupied([row-i, column+i])[1] != is_white:
                    rightTop.insert(0, "A")
                    pieceCounter = 1
                else:
                    rightTop.insert(0, "Same")
                    pieceCounter = 2
            elif pieceCounter == 1:
                if occupied([row-i, column+i])[0] == False:
                    rightTop.insert(0, "P")
                elif occupied([row-i, column+i])[1] != is_white:
                    rightTop.insert(0, "P")
                    pieceCounter = 2
                else:
                    rightTop.insert(0, "X")
                    pieceCounter = 2
            else:
                rightTop.insert(0, "X")

    pieceCounter = 0
    rightTop.append("location")

    for i in range(1, 8-row):
        if column-i >= 0:
            if pieceCounter == 0:
                if occupied([row+i, column-i])[0] == False:
                    rightTop.append("M")
                elif occupied([row+i, column-i])[1] != is_white:
                    rightTop.append("A")
                    pieceCounter = 1
                else:
                    rightTop.append("Same")
                    pieceCounter = 2
            elif pieceCounter == 1:
                if occupied([row+i, column-i])[0] == False:
                    rightTop.append("P")
                elif occupied([row+i, column-i])[1] != is_white:
                    rightTop.append("P")
                    pieceCounter = 2
                else:
                    rightTop.append("X")
                    pieceCounter = 2
            else:
                rightTop.append("X")
    pieceCounter = 0

    if singular_step == True:
        x = []
        y = []
        for i in range(-1, 1):
            x[i+1] = leftTop[(location[0]+i)]
            y[i+1] = rightTop[(location[0]+i)]
            return x, y
    else:
        return leftTop, rightTop


def horizontal(location, is_white):
    horizontalArray = []
    row, column = location

    pieceCounter = 0
    for i in range(1, column+1):
        if pieceCounter == 0:
            if occupied([row, column-i])[0] == False:
                horizontalArray.insert(0, "M")
            elif occupied([row, column-i])[1] != is_white:
                horizontalArray.insert(0, "A")
                pieceCounter += 1
            else:
                horizontalArray.insert(0, "Same")
                pieceCounter += 2
        elif pieceCounter == 1:
            if occupied([row, column-i])[0] == False:
                horizontalArray.insert(0, "P")
            elif occupied([row, column-i])[1] != is_white:
                horizontalArray.insert(0, "P")
                pieceCounter += 1
            else:
                horizontalArray.insert(0, "X")
                pieceCounter = 2
        else:
            horizontalArray.insert(0, "X")

    horizontalArray.append("location")
    pieceCounter = 0
    for i in range(column+1, 8):
        if pieceCounter == 0:
            if occupied([row, i])[0] == False:
                horizontalArray.append("M")
            elif occupied([row, i])[1] != is_white:
                horizontalArray.append("A")
                pieceCounter += 1
            else:
                horizontalArray.append("Same")
                pieceCounter += 2
        elif pieceCounter == 1:
            if occupied([row, i])[0] == False:
                horizontalArray.append("P")
            elif occupied([row, i])[1] != is_white:
                horizontalArray.append("P")
                pieceCounter += 1
            else:
                horizontalArray.append("X")
                pieceCounter = 2
        else:
            horizontalArray.append("X")
    return horizontalArray


def vertical(location, is_white):
    verticalArray = []
    row, column = location

    pieceCounter = 0
    for i in range(1, row+1):
        if pieceCounter == 0:
            if occupied([row-i, column])[0] == False:
                verticalArray.insert(0, "M")
            elif occupied([row-i, column])[1] != is_white:
                verticalArray.insert(0, "A")
                pieceCounter = 1
            else:
                verticalArray.insert(0, "Same")
                pieceCounter = 2
        elif pieceCounter == 1:
            if occupied([row-i, column])[0] == False:
                verticalArray.insert(0, "P")
            elif occupied([row-i, column])[1] != is_white:
                verticalArray.insert(0, "P")
                pieceCounter = 2
            else:
                verticalArray.insert(0, "X")
                pieceCounter = 2
        else:
            verticalArray.insert(0, "X")

    verticalArray.append("location")
    pieceCounter = 0
    for i in range(row+1, 8):
        if pieceCounter == 0:
            if occupied([i, column])[0] == False:
                verticalArray.append("M")
            elif occupied([i, column])[1] != is_white:
                verticalArray.append("A")
                pieceCounter = 1
            else:
                verticalArray.append("Same")
                pieceCounter = 2
        elif pieceCounter == 1:
            if occupied([i, column])[0] == False:
                verticalArray.append("P")
            elif occupied([i, column])[1] != is_white:
                verticalArray.append("P")
                pieceCounter = 2
            else:
                verticalArray.append("X")
                pieceCounter = 2
        else:
            verticalArray.append("X")
    return verticalArray


def moveChecker(location, x, y, is_white):
    row, column = location
    check_row, check_column = (row + x), (column + y)
    result = {}

    if ((check_row >= 0) and (check_row + x < 8) and (check_column >= 0) and (check_column < 8)):
        if occupied([check_row, check_column])[0] == False:
            result[check_row, check_column] = "M"
        elif occupied([check_row, check_column])[1] != is_white:
            result[check_row, check_column] = "A"
        else:
            result[check_row, check_column] = "S"
    else:
        result[check_row, check_column] = "X"

    return result

## checks if an location is empty, if not return the name of the piece


def occupied(array):
    for key in Board.occupied_locations:
        if Board.occupied_locations[key] == array:
            return True, Board.occupied_is_white[key]
    return [False]

## The classes of all pieces which contains their: Type, black/white, location, name


class Board:
    occupied_locations = {}
    occupied_is_white = {}
    has_moved = False
    white_type = {"rook": 1, "bischop": 1,
                  "knight": 1, "pawn": 1, "king": 1, "queen": 1}
    black_type = {"rook": 1, "bischop": 1,
                  "knight": 1, "pawn": 1, "king": 1, "queen": 1}

    def __init__(self, name, is_white, location, type):
        self.name = name
        self.is_white = is_white
        self.location = location
        Board.occupied_locations[name] = location
        Board.occupied_is_white[name] = is_white
        if is_white == True:
            Board.white_type[type] += 1
        else:
            Board.black_type[type] += 1


class Pawn(Board):
    pawn_moves = {}

    def showMoves(self):
        return self.pawn_moves

    def moves(self):
        row = self.location[0]
        column = self.location[1]

        # creates an moveing direction based on the color of the piece
        vertical = 1
        if self.is_white == False:
            vertical = -1

        ## looks for a normal move
        result = moveChecker(self.location, vertical, 0, self.is_white)
        resultRow, resultColumn = list(result.keys()), list(result.values())
        self.pawn_moves[(resultRow[0])] = resultColumn[0]
        print(self.pawn_moves)

        ## checks for dubble space opening
        if self.pawn_moves[row + vertical, column]:
            if self.has_moved == True:
                result = moveChecker(
                    self.location, (vertical + vertical), 0, self.is_white)
                resultRow, resultColumn = list(
                    result.keys()), list(result.values())
                self.pawn_moves[(resultRow[0])] = resultColumn[0]
        print(self.pawn_moves)

        ## looks for an diagonal attack
        if (occupied([row + vertical, column - 1])[0] == True) and (self.is_white != occupied([row + vertical, column - 1])):
            result = moveChecker(self.location, vertical, -1, self.is_white)
            resultRow, resultColumn = list(
                result.keys()), list(result.values())
            self.pawn_moves[(resultRow[0])] = resultColumn[0]
        if (occupied([row + vertical, column + 1])[0] == True) and (self.is_white != occupied([row + vertical, column + 1])):
            result = moveChecker(self.location, vertical, 1, self.is_white)
            resultRow, resultColumn = list(
                result.keys()), list(result.values())
            self.pawn_moves[(resultRow[0])] = resultColumn[0]
        print(self.pawn_moves)

        ## looks for enpassant attack
        if (row + vertical < 8) and (row + vertical >= 0):
            if column + 1 < 8:
                if occupied([row, column + 1])[0] == True and occupied([row, column + 1])[1] != self.is_white:
                    if occupied([row + vertical, column + 1])[0] == False:
                        result = moveChecker(
                            self.location, 0, 1, self.is_white)
                        resultRow, resultColumn = list(
                            result.keys()), list(result.values())
                        self.pawn_moves[(resultRow[0][0]+vertical),
                                        resultRow[0][1]] = "enpassant +"
            if column - 1 >= 0:
                if occupied([row, column - 1])[0] == True and occupied([row, column - 1])[1] != self.is_white:
                    if occupied([row + vertical, column - 1])[0] == False:
                        result = moveChecker(
                            self.location, 0, -1, self.is_white)
                        resultRow, resultColumn = list(
                            result.keys()), list(result.values())
                        resultRow[0][0] = resultRow[0][0] + vertical
                        self.pawn_moves[(resultRow[0][0]+vertical),
                                        resultRow[0][1]] = "enpassant -"
        print(self.pawn_moves)


class Rook(Board):
    horizontal_moves = []
    vertical_moves = []

    def showMoves(self):
        return [self.horizontal_moves, self.vertical_moves]

    def moves(self):
        self.horizontal_moves, self.vertical_moves = straight(
            self.location, self.is_white)


class Bischop(Board):
    diagonal_moves = []

    def showMoves(self):
        return self.diagonal_moves

    def moves(self):
        self.diagonal_moves = diagonal(self.location, self.is_white)


class Queen(Board):
    horizontal_moves = []
    vertical_moves = []
    diagonal_moves = []

    def showMoves(self):
        return [self.horizontal_moves, self.vertical_moves], self.diagonal_moves

    def moves(self):
        self.horizontal_moves, self.vertical_moves = straight(
            self.location, self.is_white)
        self.diagonal_moves = diagonal(self.location, self.is_white)


class King(Board):
    horizontal_moves = []
    vertical_moves = []
    diagonal_moves = []

    def showMoves(self):
        return [self.horizontal_moves, self.vertical_moves], self.diagonal_moves

    def moves(self):
        self.horizontal_moves, self.vertical_moves = straight(
            self.location, self.is_white, True)
        self.diagonal_moves = diagonal(self.location, self.is_white, True)


class Knight(Board):
    knight_moves = []
    knight_moves2 = []

    def showMoves(self):
        return self.knight_moves

    ## possible knight move secuence is the following
    ## row+2, row+1, row-2, row-1. columns starts with an + then the -
    def moves(self):
        row = self.location[0]
        column = self.location[1]

        row_array = [2, 2, 1, 1, -2, -2, -1, -1]
        column_array = [1, -1, 2, -2, 1, -1, 2, -2]

        for i in range(len(row_array)):
            if ((row + row_array[i] >= 0) and (row + row_array[i] < 8) and (column + column_array[i] >= 0) and (column + column_array[i] < 8)):
                if occupied([row + row_array[i], column + column_array[i]])[0] == False:
                    self.knight_moves.append("M")
                elif occupied([row + row_array[i], column + column_array[i]])[1] != self.is_white:
                    self.knight_moves.append("A")
                else:
                    self.knight_moves.append("S")
            else:
                self.knight_moves.append("X")
            print(row + row_array[i], column +
                  column_array[i], self.knight_moves[i])


## creates 2 arrays, one for each color. these arrays contain all of the instantiated classes of their color
white_pieces = []
black_pieces = []
for row in range(len(df.index)):
    for column in df.columns:
        if isinstance(df.iloc[row, column], str):
            if df.iloc[row, column].isupper() == True:

                if df.iloc[row, column].upper() == "P":
                    white_pieces.append(
                        Pawn(f"pawn{Board.white_type['pawn']-1}", True, [row, column], "pawn"))
                elif df.iloc[row, column].upper() == "R":
                    white_pieces.append(
                        Rook(f"rook{Board.white_type['rook']-1}", True, [row, column], "rook"))
                elif df.iloc[row, column].upper() == "B":
                    white_pieces.append(
                        Bischop(f"bischop{Board.white_type['bischop']-1}", True, [row, column], "bischop"))
                elif df.iloc[row, column].upper() == "N":
                    white_pieces.append(
                        Knight(f"knight{Board.white_type['knight']-1}", True, [row, column], "knight"))
                elif df.iloc[row, column].upper() == "K":
                    white_pieces.append(
                        King(f"king{Board.white_type['king']-1}", True, [row, column], "king"))
                elif df.iloc[row, column].upper() == "Q":
                    white_pieces.append(
                        Queen(f"queen{Board.white_type['queen']-1}", True, [row, column], "queen"))
            else:

                if df.iloc[row, column].upper() == "P":
                    black_pieces.append(
                        Pawn(f"Pawn{Board.black_type['pawn']-1}", False, [row, column], "pawn"))
                elif df.iloc[row, column].upper() == "R":
                    black_pieces.append(
                        Rook(f"Rook{Board.black_type['rook']-1}", False, [row, column], "rook"))
                elif df.iloc[row, column].upper() == "B":
                    black_pieces.append(
                        Bischop(f"Bischop{Board.black_type['bischop']-1}", False, [row, column], "bischop"))
                elif df.iloc[row, column].upper() == "N":
                    black_pieces.append(
                        Knight(f"Knight{Board.black_type['knight']-1}", False, [row, column], "knight"))
                elif df.iloc[row, column].upper() == "K":
                    black_pieces.append(
                        King(f"King{Board.black_type['king']-1}", False, [row, column], "king"))
                elif df.iloc[row, column].upper() == "Q":
                    black_pieces.append(
                        Queen(f"Queen{Board.black_type['queen']-1}", False, [row, column], "queen"))
