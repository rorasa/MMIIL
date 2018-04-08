from random import shuffle

class Block:
    def __init__(self, loc, value):
        self.loc = loc
        self.x = int(loc / 4)
        self.y = loc % 4
        self.value = value

    def move(self, direction):
        if direction=='left':
            self.moveLeft()
        elif direction=='right':
            self.moveRight()
        elif direction=='up':
            self.moveUp()
        elif direction=='down':
            self.moveDown()

    def canMoveDown(self, board):
        if self.x<3:
            if board[self.x+1][self.y] == None:
                return True
            else:
                return False
        else:
            return False

    def moveDown(self):
        if self.x <3:
            self.x = self.x+1
            self.y = self.y
            self.loc = self.x*4 + self.y

    def canMoveUp(self, board):
        if self.x >0:
            if board[self.x-1][self.y] == None:
                return True
            else:
                return False
        else:
            return False

    def moveUp(self):
        if self.x > 0:
            self.x = self.x-1
            self.y = self.y
            self.loc = self.x*4 + self.y

    def canMoveRight(self, board):
        if self.y<3:
            if board[self.x][self.y+1] == None:
                return True
            else:
                return False
        else:
            return False

    def moveRight(self):
        if self.y < 3:
            self.x = self.x
            self.y = self.y+1
            self.loc = self.x*4 + self.y

    def canMoveLeft(self, board):
        if self.y > 0:
            if board[self.x][self.y-1] == None:
                return True
            else:
                return False
        else:
            return False

    def moveLeft(self):
        if self.y >0:
            self.x = self.x
            self.y = self.y-1
            self.loc = self.x*4 + self.y

    def canMergeDown(self, board):
        if self.x <3:
            nextBlock = board[self.x+1][self.y]
            if nextBlock != None:
                if nextBlock.value == self.value:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def canMergeUp(self, board):
        if self.x >0:
            nextBlock = board[self.x-1][self.y]
            if nextBlock != None:
                if nextBlock.value == self.value:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def canMergeRight(self, board):
        if self.y <3:
            nextBlock = board[self.x][self.y+1]
            if nextBlock != None:
                if nextBlock.value == self.value:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def canMergeLeft(self, board):
        if self.y >0:
            nextBlock = board[self.x][self.y-1]
            if nextBlock != None:
                if nextBlock.value == self.value:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

class Board:
    def __init__(self):
        self.board = [[None,None,None,None],
                      [None,None,None,None],
                      [None,None,None,None],
                      [None,None,None,None]]
        self.emptyList = list(range(0,16))

    def addABlock(self):
        shuffle(self.emptyList)

        block = Block(self.emptyList[0], 1)
        self.board[block.x][block.y] = block
        self.emptyList.remove(self.emptyList[0])

    def addABlockAt(self,loc):
        block = Block(loc, 1)
        self.board[block.x][block.y] = block
        self.emptyList.remove(loc)

    def move(self, direction):
        if direction=='left':
            self.moveLeft()
        elif direction=='right':
            self.moveRight()
        elif direction=='up':
            self.moveUp()
        elif direction=='down':
            self.moveDown()

    def moveDown(self):
        movedCount = 0
        for row in self.board:
            for block in row:
                if block != None:
                    if block.canMergeDown(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        self.board[block.x+1][block.y].value += block.value

                        movedCount = movedCount + 1
                    elif block.canMoveDown(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        block.moveDown()

                        self.board[block.x][block.y] = block
                        self.emptyList.remove(block.x*4 + block.y)

                        movedCount = movedCount + 1

        if movedCount > 0:
            self.moveDown()

    def moveUp(self):
        movedCount = 0
        for row in self.board:
            for block in row:
                if block != None:
                    if block.canMergeUp(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        self.board[block.x-1][block.y].value += block.value

                        movedCount = movedCount + 1
                    elif block.canMoveUp(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4+block.y)

                        block.moveUp()

                        self.board[block.x][block.y] = block
                        self.emptyList.remove(block.x*4 + block.y)

                        movedCount = movedCount + 1

        if movedCount > 0:
            self.moveUp()

    def moveRight(self):
        movedCount = 0
        for row in self.board:
            for block in row:
                if block != None:
                    if block.canMergeRight(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        self.board[block.x][block.y+1].value += block.value

                        movedCount = movedCount + 1
                    elif block.canMoveRight(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        block.moveRight()

                        self.board[block.x][block.y] = block
                        self.emptyList.remove(block.x*4 + block.y)

                        movedCount = movedCount + 1

        if movedCount > 0:
            self.moveRight()

    def moveLeft(self):
        movedCount = 0
        for row in self.board:
            for block in row:
                if block != None:
                    if block.canMergeLeft(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        self.board[block.x][block.y-1].value += block.value

                        movedCount = movedCount + 1
                    elif block.canMoveLeft(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        block.moveLeft()

                        self.board[block.x][block.y] = block
                        self.emptyList.remove(block.x*4 + block.y)

                        movedCount = movedCount + 1

        if movedCount > 0:
            self.moveLeft()

    def prettyPrint(self):
        for i in range(0,4):
            print("| ", end='')
            for j in range(0,4):
                block = self.board[i][j]
                if block != None:
                    print(str(block.value)+" | ", end='')
                else:
                    print(" | ", end='')
            print("\n-------------")

if __name__=='__main__':
    print("Hello World")

    board = Board()
    board.addABlockAt(0)
    board.addABlockAt(4)
    print(board.emptyList)
    board.prettyPrint()

    board.moveUp()
    print(board.emptyList)
    board.prettyPrint()

    board.addABlockAt(2)

    board.moveDown()
    print(board.emptyList)
    board.prettyPrint()

    board.moveRight()
    print(board.emptyList)
    board.prettyPrint()

    board.addABlockAt(7)
    print(board.emptyList)
    board.prettyPrint()

    board.moveDown()
    print(board.emptyList)
    board.prettyPrint()§

    board.moveLeft()
    print(board.emptyList)
    board.prettyPrint()
