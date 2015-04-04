#!/usr/bin/python3

import os
import requests
import sys
import json
import random
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory, connectWS
from twisted.internet import reactor, ssl
from twisted.python import log
from game.chess import Chess
from game.boardImage import BoardImage
from slackRequests import SlackRequests

class SocketClient(WebSocketClientProtocol):
  slackRequests = SlackRequests(os.environ['SLACKAPI'])
  games = {}

  def __init__(self):
    #if running in docker
    try:
      os.chdir('/slackChess/')
    except IOError:
      pass

    with open('config.json') as f:
      j = json.load(f)
    imgDir = j['imageDir']
    self.boardImage = BoardImage(imgDir)
    Chess.imgURL = j['imageURL']

  def onConnect(self, response):
    print("Server connected: {0}".format(response.peer))

  def onOpen(self):
    print("WebSocket connection open.")

  def parseMessage(self, msg):
    text = msg['text']
    coms = text.split(' ')
    if coms[0] == '$chess':
      channelID = msg['channel']
      userID = msg['user']

      if len(coms) > 1 and coms[1] == 'new':
        if channelID in self.games:
          self.sendResponse('Game already in progress.', channelID)
        elif len(coms) == 3:
          userInvite = self.slackRequests.checkUsername(coms[2])
          whiteName = self.slackRequests.getUserName(userID)
          if userInvite is None or whiteName is None:
            return
          userInviteID = userInvite['id']
          userInviteName = userInvite['name']
          didInvite = self.slackRequests.inviteUser(userInviteID, channelID)
          if didInvite:
            game = Chess(whiteName, userID, userInviteName, userInviteID, self.boardImage)
            self.sendResponse('Setting up game...', channelID)
            self.sendResponse(game.boardLink + "\n" + game.atMsg[userID] + "You're first.", channelID)
            self.games[channelID] = game

      elif len(coms) > 1 and coms[1] == 'move':
        if channelID in self.games:
          if len(coms) == 3:
            move = coms[2]
            game = self.games[channelID]
            resp = game.makeMove(userID, move)
            self.sendResponse(resp, channelID)

        
  def sendResponse(self, msg, channelID):
    chatID = random.randint(0, 100000)
    response = {
      'id': chatID,
      'type': 'message',
      'channel': channelID,
      'text': msg
    }
    jsonStr = json.dumps(response).encode('utf-8')
    self.sendMessage(jsonStr)

  def onMessage(self, payload, isBinary):
    msg = json.loads(payload.decode('utf-8'))
    print(msg)

    if 'ok' in msg:
      return
    
    command = msg['type']
    if command == 'message' and 'text' in msg:
      self.parseMessage(msg)

  def onClose(self, wasClean, code, reason):
    print("WebSocket connection closed: {0}".format(reason))

if __name__ == '__main__':
  token = os.environ['SLACKBOT']
  baseURL = 'https://slack.com/api/rtm.start'
  params = {'token': token}
  response = requests.post(baseURL, data=params)
  respJSON = response.json()

  if not respJSON['ok']:
    print('Authentication failed.')
    sys.exit(0)

  wss = respJSON['url']

  log.startLogging(sys.stdout)

  factory = WebSocketClientFactory(wss, debug=False) 
  factory.protocol = SocketClient
  contextFactory = ssl.ClientContextFactory()

  connectWS(factory, contextFactory)

  reactor.run()
