# TTS Radio
TTS Radio is a python program that plays .wav songs and announces the names of the songs via TTS

## Opperation out of the box.
For this program to work, you need to install pywin32. You can do this via pip.
Open cmd and enter:
```bash
pip install pywin32
```

Insert your music of .wav format into the sounds folder. Launch radio.py to start listening.

## Customisation
You can customise the messages by oppening the config.py file and changing the values. For example:
```py
announcement = ("You're listening to Text to Speech Radio.")
```
could be changed to
```py
announcement = ("This is my awesome radio station!")
```
On some phrases, you can customise the front and back of the message.
```py
justPlayed1 = ("That was ")
#               songname
justPlayed2 = (".")
```
This could be changed to:
```py
justPlayed1 = ("That song you heard was ")
#               songname
justPlayed2 = (". Pretty cool!")
```
What would be said is, "That song you just heard was [songname]. Pretty cool!"

## Compatability
This software will only opperate properly on Windows.

This software has been tested to run on Windows 10 and with python 3.8.6

Currently, the only audio format supported is .wav, or any format compatible with winsound. This choice was made because of compatibility issues and the audio not being able to load with the playsound module.

## Copyright
Copyright (c) 2020 [Aconix](https://streamerlinks.com/Aconix)
