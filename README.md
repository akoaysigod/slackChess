# Slack Chess

This is a bot for playing multiplayer chess games on Slack.

Usage:

```
$chess new [opponentName]
$chess move [a-h1-8a-h1-8]
```

It also accepts other chess notations for moves but I don't really understand chess notation very well or chess for that matter.

You need two environment variables for this to work

```bash
export SLACKBOT=slackBotAPIKey
export SLACKAPI=slackAPIKey
```

In config.json you can specify where there image files are located and also where the images will be served from.
I was going to add a simple get request server but I haven't yet. Right now I'm just using Nginx to serve the image files.

# dependencies

twisted

autobahn

pyopenssl

python-chess

pillow

# docker

The Dockerfile has a complete list of everything that needs to be installed in order to get this running.

To run the Dockerfile I'm using this command:

```bash
sudo docker run -e SLACKBOT=$SLACKBOT -e SLACKAPI=$SLACKAPI -v /path/to/images/:/resources/ imagename
```

# todo

Build a standalone server to serve images maybe

Add an option to display a text based board rather than images

Manage images in a nicer way.

Connect to a DB and/or Reddis just in case something happens or to replay games, etc. Anything really I just want to set it up at some point for fun.

Castling. The library supports it but I forgot to check how it works. 

#screenshot

![ALT text](/screenshot.png)
