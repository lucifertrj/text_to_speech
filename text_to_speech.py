import pyttsx3 as ts
import time

speak = ts.init()

name=input('Enter name:')
greet=input('How you feel today?').lower()
speak.say('Hello')
time.sleep(2)

speak.say('I am Lucifer')

time.sleep(2)

speak.say(f'I repeat whatever {name} tells')
time.sleep(2)

if 'good' in greet or 'cool' in greet or 'great' in greet:
	speak.say('ok, have a nice day')
else:
	speak.say('Better luck next time')

speak.runAndWait()




