import json
from PIL import Image
from game.pieces import Black, White

class BoardImage:
  def __init__(self, imgDir):
    self.imgDir = imgDir
    
    piecePath = self.imgDir + 'images/'
    self.pieces = {
      'P': Image.open(piecePath + 'whitePawn.png'),
      'R': Image.open(piecePath + 'whiteRook.png'),
      'N': Image.open(piecePath + 'whiteKnight.png'),
      'B': Image.open(piecePath + 'whiteBishop.png'),
      'K': Image.open(piecePath + 'whiteKing.png'),
      'Q': Image.open(piecePath + 'whiteQueen.png'),
      'p': Image.open(piecePath + 'blackPawn.png'),
      'r': Image.open(piecePath + 'blackRook.png'),
      'n': Image.open(piecePath + 'blackKnight.png'),
      'b': Image.open(piecePath + 'blackBishop.png'),
      'k': Image.open(piecePath + 'blackKing.png'),
      'q': Image.open(piecePath + 'blackQueen.png')
    }

  def closeFiles(self):
    for k in self.pieces:
      self.pieces[k].close()
   
  def translateCoordinates(self, x, y):
    rX = 60 * (x + 1)
    rY = 60 * (y + 1)
    return (rX, rY)

  def create(self, gameID, board, isBlack):
    outImage = self.imgDir + 'boards/' + gameID + '.png'
    boardPath = self.imgDir + 'images/board.png'
    boardImg = Image.open(boardPath)

    bStr = board.__str__().split('\n')
    bArr = [z.split(' ') for z in bStr]

    for (y, row) in enumerate(bArr):
      for (x, p) in enumerate(row):
        if p == '.':
          continue
        img = self.pieces[p]
        pos = self.translateCoordinates(x, y)

        if isBlack:
          img = img.rotate(180)
        boardImg.paste(img, pos, img)
    if isBlack:
      boardImg = boardImg.rotate(180)
    boardImg.save(outImage)
