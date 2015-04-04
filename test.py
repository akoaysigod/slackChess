#!/usr/bin/python3

from game.boardImage import BoardImage
from game.chess import Chess
import chess
import unittest


class Tests(unittest.TestCase):

  def testIllegalTurn(self):
    x = "@name2: It's not your turn."
    m = self.c.makeMove('2', 'e7e5')
    self.assertEqual(x, m)

  def testIllegalMove(self):
    x = "That is not a legal move."
    m = self.c.makeMove('1', 'e7e5')
    self.assertEqual(x, m)

  def testLegalMove(self):
    x = "@name2: It's your turn."
    m = self.c.makeMove('1', 'e2e4')
    m = m.split("\n")
    self.assertEqual(x, m[1])

  def testCheckmate(self):
    x = '@name1: Checkmate! You win.'
    self.c.makeMove('1', 'e2e4')
    self.c.makeMove('2', 'e7e5')
    self.c.makeMove('1', 'd1h5')
    self.c.makeMove('2', 'b8c6')
    self.c.makeMove('1', 'f1c4')
    self.c.makeMove('2', 'g8f6')
    m = self.c.makeMove('1', 'h5f7')
    m = m.split("\n")

    self.assertEqual(x, m[1])

  def testCheck(self):
    x = "Check."
    self.c.makeMove('1', 'e2e4')
    self.c.makeMove('2', 'a7a5')
    self.c.makeMove('1', 'e4e5')
    self.c.makeMove('2', 'a5a4')
    self.c.makeMove('1', 'e5e6')
    self.c.makeMove('2', 'a4a3')
    m = self.c.makeMove('1', 'e6d7')
    m = m.split('\n')
    
    self.assertEqual(x, m[1])

  #was hoping this would stop the ResourceWarning
  def setUp(self):
    self.b = BoardImage()
    self.c = Chess('name1', '1', 'name2', '2', self.b)

  def tearDown(self):
    self.b.closeFiles()

if __name__ == '__main__':
  unittest.main()
