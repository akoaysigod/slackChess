import requests

class SlackRequests:
  baseURL = 'https://slack.com/api/'
  def __init__(self, token):
    self.token = token
  
  def makeRequest(self, endPoint, params):
    url = self.baseURL + endPoint
    params['token'] = self.token
    req = requests.post(url, data=params)
    return req.json()

  def getUserName(self, userID):
    params = {'user': userID}
    resp = self.makeRequest('users.info', params)
    if resp['ok']:
      return resp['user']['name']
    else:
      print(resp)
      return None


  def checkUsername(self, username):
    resp = self.makeRequest('users.list', {})
    if not resp['ok']:
      print(resp)
      return None
    else:
      for user in resp['members']:
        if user['name'] == username:
          return user
      return None
      
  def inviteUser(self, userID, channelID):
    params = {'user': userID, 'channel': channelID}
    resp = self.makeRequest('groups.invite', params)
    if not resp['ok']:
      print(resp)
      return False
    return True
