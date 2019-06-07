import time
import os
import speech_recognition as sr
import gtts

def listen():
	try:
		r = sr.Recognizer()
		mic = sr.Microphone()

		print('Listening..........')
		with mic as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
		print('Understood')
		query = r.recognize_google(audio)

		print(query)
		return query
	except:

		print("I dont understand.....")
		time.sleep(.7)
		os.system('cls')
		return ""
    
def say(text):
	sleepTime = len(text)/3
	resp = gTTS(text = text, lang = 'en', slow = False)
	resp.save('audio.mp3')
	os.system('audio.mp3')
	time.sleep(sleepTime)
