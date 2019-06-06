from selenium import webdriver
import bs4 
from urllib.request import urlopen
import speech_recognition as sr
import os
import time

browser = webdriver.Chrome("chromedriver")

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

def startup():
	state = listen().upper()

	while state != 'HEY WIZKID':
		startup()

	main()

def main():
	global browser
	# new, top, or mix url
	track_url = "https://soundcloud.com/search/sounds?q="
	artist_url = "https://soundcloud.com/search/people?q="

	# create the selenium browser
	browser = webdriver.Chrome("chromedriver")

	choice = str(listen())

	choiceArr = choice.split()

	#fuck
	

	while choice == "":
		choice = str(listen())

	choice = "%20".join(choice.split())
	print(choice)

	resp = urlopen(track_url + choice)
	if resp.getcode() == 200:
		soup = bs4.BeautifulSoup(resp.read(), "html")

		print('--------------------------------------------------')
		print('---------------------------------------------------')

		songs = soup.select("a[href]")[2:]
		print(songs)
		songLinks =[]

		for index, song in enumerate(songs):
			songLinks.append(song.get("href"))

		browser.get('https://soundcloud.com' + songLinks[4])

		startup()


if __name__ == '__main__':
	startup()
       
