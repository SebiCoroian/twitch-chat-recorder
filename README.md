# Twitch chat recorder
## _simple tool for recording your twitch chat_

This is a simple python program that once configured and ran will save your livestream chat logs in a JSON format as well as in a video format. <br/>

## configuration

We're connecting to the host via Python socket. <br/>
In [config.py](config.py), the connection details for Twitch are already set. What needs to be changed is the twitch authentication token, the nickname and the channel. <br/>
You can get a token for your account at https://twitchapps.com/tmi/ and it should look somewhat like this:
`oauth:ferdn2jzqj2ncs6jpuddkfa0wdx7qe`
<br/>
For additional config information visit https://dev.twitch.tv/docs/irc/join-chat-room <br/>
<br/>

## [logger.py](logger.py)

The logger is the tool you're running during the livestream in order to record chats in a JSON format

The JSON chat object contains the following:
- _username_ - Twitch username of the publisher 
- _time_ - Timestamp of the chat message
- _message_ - Content of the chat message

## [emulator.py](emulator.py)

Emulator is the tool that is ran afterwards. Using the contents of the JSON file previously created, it will generate a real-time livestream window video as shown below:

![Alt Text](https://github.com/SebiCoroian/twitch-chat-recorder/blob/main/demo.gif)

The output is displayed on a green solid color so you can easily remove and overlay on your raw video. <br/>
This is done by generating and merging together individual frames of the chats. If needed, these are saved by default in `/images/` subfolder.<br/><br/>

Enjoy!
