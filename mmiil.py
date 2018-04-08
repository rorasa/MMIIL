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
        isMoved = False
        for row in self.board:
            for block in row:
                if block != None:
                    if block.canMergeDown(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        self.board[block.x+1][block.y].value += block.value

                        movedCount = movedCount + 1
                        isMoved = True
                    elif block.canMoveDown(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        block.moveDown()

                        self.board[block.x][block.y] = block
                        self.emptyList.remove(block.x*4 + block.y)

                        movedCount = movedCount + 1
                        isMoved = True

        if movedCount > 0:
            self.moveDown()

        return isMoved

    def moveUp(self):
        movedCount = 0
        isMoved = False
        for row in self.board:
            for block in row:
                if block != None:
                    if block.canMergeUp(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        self.board[block.x-1][block.y].value += block.value

                        movedCount = movedCount + 1
                        isMoved = True
                    elif block.canMoveUp(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4+block.y)

                        block.moveUp()

                        self.board[block.x][block.y] = block
                        self.emptyList.remove(block.x*4 + block.y)

                        movedCount = movedCount + 1
                        isMoved = True

        if movedCount > 0:
            self.moveUp()

        return isMoved

    def moveRight(self):
        movedCount = 0
        isMoved = False
        for row in self.board:
            for block in row:
                if block != None:
                    if block.canMergeRight(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        self.board[block.x][block.y+1].value += block.value

                        movedCount = movedCount + 1
                        isMoved = True
                    elif block.canMoveRight(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        block.moveRight()

                        self.board[block.x][block.y] = block
                        self.emptyList.remove(block.x*4 + block.y)

                        movedCount = movedCount + 1
                        isMoved = True

        if movedCount > 0:
            self.moveRight()

        return isMoved

    def moveLeft(self):
        movedCount = 0
        isMoved = False
        for row in self.board:
            for block in row:
                if block != None:
                    if block.canMergeLeft(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        self.board[block.x][block.y-1].value += block.value

                        movedCount = movedCount + 1
                        isMoved = True
                    elif block.canMoveLeft(self.board):
                        self.board[block.x][block.y] = None
                        self.emptyList.append(block.x*4 + block.y)

                        block.moveLeft()

                        self.board[block.x][block.y] = block
                        self.emptyList.remove(block.x*4 + block.y)

                        movedCount = movedCount + 1
                        isMoved = True

        if movedCount > 0:
            self.moveLeft()

        return isMoved

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

class Game:
    def __init__(self):
        self.board = Board()
        self.turns = 0
        self.goal = 2048
        self.won = False

        self.board.addABlock()

    def checkWinning(self):
        isWon = False
        for row in self.board.board:
            for block in row:
                if block != None:
                    if block.value == self.goal:
                        isWon = True
        return isWon

    def move(self, direction):
        if self.won == True:
            return False

        if direction == 'up':
            self.board.moveUp()
        elif direction == 'down':
            self.board.moveDown()
        elif direction == 'right':
            self.board.moveRight()
        elif direction == 'left':
            self.board.moveLeft()
        else:
            raise ValueError('Direction must be up, down, left, or right.')

        self.board.addABlock()

        self.turns += 1

        if self.checkWinning():
            self.won = True

        return True


if __name__=='__main__':
    print("MMIIL")

    game = Game()
    game.board.prettyPrint()

    while not game.won:
        nextMove = input('Up(w), Down(s), Left(a), Right(d): ')
        if nextMove=='w':
            game.move('up')
        elif nextMove=='s':
            game.move('down')
        elif nextMove=='a':
            game.move('left')
        elif nextMove=='d':
            game.move('right')
        game.board.prettyPrint()

    print("You WIN!")
    print("Total turns: "+str(game.turns))
