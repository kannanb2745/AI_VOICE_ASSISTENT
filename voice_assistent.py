import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import turtle
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import instaloader
import ctypes
import time
import requests
import shutil
from sketchpy import canvas
from sketchpy import library as lib
from turtle import *
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname ="simple ai bot"
	speak("I am your Assistant")
	speak(assname)
	

def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
     
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('your email id', 'your email password')
	server.sendmail('your email id', to, content)
	server.close()
if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()
	wishMe()
	username()
	
	while True:
		
		query = takeCommand().lower()
		
		# All the commands said by user will be
		# stored here in 'query' and will be
		# converted to lower case for easily
		# recognition of command
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow Happy coding")
			webbrowser.open("stackoverflow.com")

		elif 'today time' in query or 'what is the time now' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir, the time is {strTime}")

		elif 'open opera' in query:
			codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
			os.startfile(codePath)

		elif 'email to kannan' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				to = "Receiver email address"
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'send a mail' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				speak("whome should i send")
				to = input()
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by MR KANNAN.")
			
		elif 'tell me an joke' in query:
			speak(pyjokes.get_joke())
			
		elif "calculate" in query:
			
			app_id = "Wolframalpha api id"
			client = wolframalpha.Client(app_id)
			indx = query.lower().split().index('calculate')
			query = query.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			print("The answer is " + answer)
			speak("The answer is " + answer)
		elif 'instagram details' in query:
			ig=instaloader.Instaloader()
			speak("tell the user name of that insta id")
			usrname=input('enter user name\n')
			profile=instaloader.Profile.from_username(ig.context, usrname)
			speak("Username is ")
			speak(profile.username)
			speak("Number of Posts Uploaded are")
			speak(profile.mediacount)
			speak(" he or she is having ")
			speak(profile.followers)
			speak(' followers')
			speak(" he or she is following ")
			speak(profile.followees)
			speak('people')
			speak("he or she Bio is ")
			speak(profile.biography)
		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query:
			speak("If you talk then definitely your human.")

		elif "why you came to world" in query:
			speak("Thanks to KANNAN. further It's a secret")

		elif 'open power point presentation' in query:
			speak("opening Power Point presentation")
			power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
			os.startfile(power)

		elif 'what is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant created by KANNAN")

		elif 'reason for you' in query:
			speak("I was created as a Minor project by Mister KANNAN ")

		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,
													0,
													"Location of wallpaper",
													0)
			speak("Background changed successfully")

		elif 'open bluestack' in query:
			appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
			os.startfile(appli)

		elif 'news' in query:
			
			try:
				jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
				data = json.load(jsonObj)
				i = 1
				
				speak('here are some top news from the times of india')
				print('''=============== TIMES OF INDIA ============'''+ '\n')
				
				for item in data['articles']:
					
					print(str(i) + '. ' + item['title'] + '\n')
					print(item['description'] + '\n')
					speak(str(i) + '. ' + item['title'] + '\n')
					i += 1
			except Exception as e:
				
				print(str(e))

		
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")

		elif "camera" in query or "take a photo" in query:
			ec.capture(0, "Jarvis Camera ", "img.jpg")

		elif "restart the system" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt", "r")
			print(file.read())
			speak(file.read(6))

		elif 'counting number' in query:
			speak("tell me the number when i want to stop ")
			num=int(takeCommand())
			for i in range(1,num+1):
				speak(i)
		elif "calculator" in query:
			speak("choose any one the option below:\n")
			print("1.Addition:\n 2.subtraction:\n 3.multiplication:\n 4.division:\n")
			n=takeCommand()
			if (n=='addition') or (n=='one') or (n==1):
				speak("give me two number of input")
				speak("tell me the first value ")
				A=int(takeCommand())
				speak("tell me the seconde value")
				B=int(takeCommand())
				add=A+B
				print("the addition of first and seconde value is :",add)
				speak("the addition of first and seconde value is :")
				speak(add)
			elif (n=='subtraction') or (n==2) or (n=='two'):
				speak("give me two number of input")
				speak("tell me the first value ")
				A=int(takeCommand())
				speak("tell me the seconde value")
				B=int(takeCommand())
				sub=A-B
				print("the subtraction of first and seconde value is :",sub)
				speak("the subtraction of first and seconde value is ")
				speak(sub)
			elif (n=='multiplication') or (n==3) or (n=='three'):
				speak("give me two number of input")
				speak("tell me the first value ")
				A=int(takeCommand())
				speak("tell me the seconde value")
				B=int(takeCommand())
				mul=A*B
				print("the multiplication of first and seconde value is :",mul)
				speak("the multiplication of first and seconde value is ")
				speak(mul)
			elif (n=='division') or (n==4) or (n=='four'):
				speak("give me two number of input")
				speak("tell me the first value ")
				A=int(takeCommand())
				speak("tell me the seconde value")
				B=int(takeCommand())
				div=A/B
				print("the division of first and seconde value is :",div)
				speak("the division of first and seconde value is")
				speak(div)
			else:
				speak("are you kidding me")
				speak("please give input present in list")
		elif 'draw national flag' in query:
			#screen for output
			screen = turtle.Screen()
			# Defining a turtle Instance
			t = turtle.Turtle()
			t.speed(2)
			# initially penup()
			t.penup()
			t.goto(-400, 250)
			t.pendown()
			# Orange Rectangle
			#white rectangle
			t.color("orange")
			t.begin_fill()
			t.forward(800)
			t.right(90)
			t.forward(167)
			t.right(90)
			t.forward(800)
			t.end_fill()
			t.left(90)
			t.forward(167)
			# Green Rectangle
			t.color("green")
			t.begin_fill()
			t.forward(167)
			t.left(90)
			t.forward(800)
			t.left(90)
			t.forward(167)
			t.end_fill()
			# Big Blue Circle
			t.penup()
			t.goto(70, 0)
			t.pendown()
			t.color("navy")
			t.begin_fill()
			t.circle(70)
			t.end_fill()
			# Big White Circle
			t.penup()
			t.goto(60, 0)
			t.pendown()
			t.color("white")
			t.begin_fill()
			t.circle(60)	
			t.end_fill()
			#	 Mini Blue Circles
			t.penup()
			t.goto(-57, -8)
			t.pendown()
			t.color("navy")
			for i in range(24):
				t.begin_fill()
				t.circle(3)
				t.end_fill()
				t.penup()
				t.forward(15)
				t.right(15)
				t.pendown()
				# Small Blue Circle
			t.penup()
			t.goto(20, 0)
			t.pendown()
			t.begin_fill()
			t.circle(20)
			t.end_fill()
			# Spokes
			t.penup()
			t.goto(0, 0)
			t.pendown()
			t.pensize(2)
			for i in range(24):
				t.forward(60)
				t.backward(60)
				t.left(15)
				#to hold the
				#output window
			turtle.done()
		elif 'draw abdul kalam sir ' in query or 'draw apj adul kalam sir' in query or "abdul kalam" in query or 'draw abdul kalam' in query:
				obj= lib.apj()
				obj.pen.speed(2)
				obj.draw()
		elif 'draw iron man' in query or 'draw tony stark' in query or 'iorn man' in query:
				obj1=lib.rdj()
				obj1.pen.speed(2)
				obj1.draw()
		elif 'draw me' in query or 'draw kannan' in query:
			obj2=canvas.sketch_from_image('C:\\Users\\kanna\\OneDrive\\Pictures\\Screenshot_20221223_141632.jpg')
			obj2.draw(threshold=127)
		elif 'draw my sketch' in query:
			obj3 =canvas.sketch_from_svg("C:\\Users\\kanna\\Downloads\\Screenshot_20221223_141632.svg",scale =250)
			obj3.draw()
		elif 'draw my gang' in query:
			obj4=canvas.sketch_from_image("C:\\Users\\kanna\\OneDrive\\Pictures\\Screenshot_20230112_175240.jpg")
			obj4.draw(threshold=127)
		elif 'draw my dog' in query:
			obj5=canvas.sketch_from_image("C:\\Users\\kanna\\OneDrive\\Pictures\\IMG_20221113_124805_407.jpg")
			obj5.draw(threshold=127)
		elif 'draw vijay' in query:
			obj6=lib.vijay()
			obj6.draw()
		elif "update assistant" in query:
			speak("After downloading file please replace this file with the downloaded one")
			url = '# url after uploading file'
			r = requests.get(url, stream = True)
			
			with open("Voice.py", "wb") as Pypdf:
				
				total_length = int(r.headers.get('content-length'))
				
				for ch in progress.bar(r.iter_content(chunk_size = 2391975),
									expected_size =(total_length / 1024) + 1):
					if ch:
						Pypdf.write(ch)
					
		# NPPR9-FWDCX-D2C8J-H872K-2YT43
		elif "jarvis" in query:
			
			wishMe()
			speak("Jarvis 1 point o in your service Mister")
			speak(assname)

		elif "weather" in query:
			
			# Google Open weather website
			# to get API of Open weather
			api_key = "Api key"
			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
			speak(" City name ")
			print("City name : ")
			city_name = takeCommand()
			complete_url = base_url + "appid =" + api_key + "&q =" + city_name
			response = requests.get(complete_url)
			x = response.json()
			
			if x["code"] != "404":
				y = x["main"]
				current_temperature = y["temp"]
				current_pressure = y["pressure"]
				current_humidiy = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
			
			else:
				speak(" City Not Found ")
			
		elif "send message " in query:
				# You need to create an account on Twilio to use this service
				account_sid = 'Account Sid key'
				auth_token = 'Auth token'
				client = Client(account_sid, auth_token)

				message = client.messages \
								.create(
									body = takeCommand(),
									from_='Sender No',
									to ='Receiver No'
								)

				print(message.sid)

		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")
		elif "tell about you" in query or "self introduction" in query:
			speak("The primary purpose of developing voice recognition software is to make everyday life easier in business and private life. Voice assistants can perform many tasks for your business while you are occupied with something else. In addition, they can replace a human being in completing specific tasks, such as: answering questions, making calls, creating to-do lists, and much more. They, therefore, allow you to save time and help you multitask. ")

		elif "Good Morning " in query or "Good afternoon" in query or "Good evening" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(username)

		# most asked question from google Assistant
		elif "will you be my gf" in query or "will you be my bf" in query:
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine, about you")

		elif "i love you" in query:
			speak("I love you too")
			speak(username)

		elif "what is" in query or "who is" in query:
			
			# Use the same API key
			# that we have generated earlier
			client = wolframalpha.Client("API_ID")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")
		
		
		
		# elif "" in query:
			# Command go here
			# For adding more commands
