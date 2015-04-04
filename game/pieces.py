from enum import Enum

class Black(Enum):
  pawn = 0
  rook = 1
  knight = 2
  bishop = 3
  queen = 4
  king = 5

class White(Enum):
  pawn = 0
  rook = 1
  knight = 2
  bishop = 3
  queen = 4
  king = 5

class CheckMove():
  def __init__(self, board):
    self.board = board

  def checkFirst(self, start, end):
    if len(start) != 2 or len(end) != 2:
      return False
    if ord(start[0]) < 97 or ord(start[0]) > 104:
      return False
    if ord(end[0]) < 97 or ord(end[0]) > 104:
      return False
    if ord(start[1]) < 49 or ord(start[1]) > 56:
      return False
    if ord(end[1]) < 49 or ord(end[1]) > 56:
      return False
    if start not in self.board[start]:
      return False
    if self.board[start] is None:
      return False

    if type(self.board[start]) is type(self.board[end]):
      return False

    return True

  def checkPawn(self, start, end):
    x, y = ord(start[0]), ord(start[1])
    eX, eY = ord(end[0]), ord(end[1])


    return True
