# Twitch chat recorder
## _simple tool for logging your twitch chat_

This is a simple python program that once configured and ran will save your livestream chat logs in a JSON format. <br>
The JSON chat object contains the following:
- _username_ - Twitch username of the publisher 
- _time_ - Timestamp of the chat message
- _message_ - Content of the chat message

## configuration

We're connecting to the host via Python socket. <br>
In config.py, the connection details for Twitch are already set. What needs to be changed is the twitch authentication token, the nickname and the channel. <br>
You can get a token for your account at https://twitchapps.com/tmi/ and it should look somewhat like this:
`oauth:ferdn2jzqj2ncs6jpuddkfa0wdx7qe`
For additional config information visit https://dev.twitch.tv/docs/irc/join-chat-room <br>
<br>
Enjoy!
