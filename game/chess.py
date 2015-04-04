import random
import chess
import json

class Chess:
  gameID = str(random.randint(0, 100000))
  imgURL = ''

  @property
  def boardLink(self):
    return self.imgURL + self.gameID + '.png'

  def __init__(self, whiteName, whiteID, blackName, blackID, boardImage):
    self.board = chess.Board()
    self.boardImage = boardImage
    
    self.turn = whiteID
    self.whiteName = whiteName
    self.whiteID = whiteID
    self.blackName = blackName
    self.blackID = blackID

    self.atMsg = {whiteID: "@" + whiteName + ": ",
                  blackID: "@" + blackName + ": "}
    
    self.createBoard()

  def createBoard(self):
    gameID = int(self.gameID)
    gameID += 1
    self.gameID = str(gameID)
    self.boardImage.create(self.gameID, self.board, self.board.turn)

  def setTurn(self):
    if self.board.turn == 0:
      self.turn = self.blackID
    else:
      self.turn = self.whiteID

  def getMove(self, move):
    try:
      m = chess.Move.from_uci(move)
      return m
    except ValueError:
      return None

  def makeMove(self, player, move):
    if player != self.turn:
      return self.atMsg[player] + "It's not your turn."

    move = move.lower()
    move = self.getMove(move)
    if move is None:
      return "Invalid input. Format: [a-h][1-8][a-h][1-8]"

    if move not in self.board.legal_moves:
      return "That is not a legal move."

    self.setTurn()
    self.board.push(move)
    self.createBoard()

    msg = self.boardLink + "\n" 
    if self.board.is_checkmate():
      self.setTurn()
      msg += self.atMsg[self.turn] + "Checkmate! " + "You win.\n" 
    elif self.board.is_check():
      msg += "Check.\n"
    elif self.board.is_insufficient_material():
      msg += "Not enough pieces left. Draw.\n"
    elif self.board.is_stalemate():
      msg += "Draw.\n"
    else:
      msg += self.atMsg[self.turn] + "It's your turn.\n"

    msg += "Turn Count: " + str(self.board.fullmove_number)
    return msg
