from selenium import webdriver
import bs4 
from urllib.request import urlopen
import speech_recognition as sr
import os
import time
import WizSpeak

browser = webdriver.Chrome("chromedriver")

def startup():
	state = listen().upper()

	while state != 'HEY WIZKID':
		say('How can I help you')
		startup()

	main()

def main():
	global browser
	# new, top, or mix url
	track_url = "https://soundcloud.com/search/sounds?q="
	artist_url = "https://soundcloud.com/search/people?q="
	joji_url = "https://soundcloud.com/boulon-roger/sets/joji"
	cityPop_url = "https://soundcloud.com/boulon-roger/sets/city-pop"

	# create the selenium browser
	browser = webdriver.Chrome("chromedriver")

	choice = str(listen())
	

	while choice == "":
		choice = str(listen())
		
	choiceArr = choice.split().upper()
	
	for keyWord in choiceArr:
		if keyWord == 'PLAYLIST':
			for keyWord in choiceArr:
				if keyWord == 'JOJI':
					browser.get(joji_url)
				elif keyWord == 'CITY':
					browser.get(cityPop_url)
		else:
			

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
       
