#Internet Connectivity Checker 
import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
if connect():
    print("Connected to Internet")
else:
    print("No Internet! Connect your Device with Internet first :( ") 

    quit()


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import time
import smtplib
import subprocess
import shutil
import winshell
import ctypes
#import win32com.client as wincl 
#from bs4 import BeautifulSoup
from ssl import OP_ENABLE_MIDDLEBOX_COMPAT
from tkinter import * 
from tkinter import messagebox
from PIL import Image



    
def SelfIntro():

    import pyglet
 
    # width of window
    width = 1280
    
    # height of window
    height = 720
    
    # caption i.e title of the window
    title = "Intro Video"
    
    # creating a window
    window = pyglet.window.Window(width, height, title)
    
    
    # video path
    vidPath ="\\Project\\ZOYA GUI\\Videos\\1.mp4"
    
    # creating a media player object
    player = pyglet.media.Player()
    
    # creating a source object
    source = pyglet.media.StreamingSource()
    
    # load the media from the source
    MediaLoad = pyglet.media.load(vidPath)
    
    # add this media in the queue
    player.queue(MediaLoad)
    
    # play the video
    player.play()
    
    # on draw event
    @window.event
    def on_draw():
        
        # clea the window
        window.clear()
        
        # if player source exist
        # and video format exist
        if player.source and player.source.video_format:
            
            # get the texture of video and
            # make surface to display on the screen
            player.get_texture().blit(0, 0)

    # key press event    
    @window.event
    def on_key_press(symbol, modifier):
    
        # key "p" get press
        if symbol == pyglet.window.key.P:
            
            # pause the video
            player.pause()
            
            # printing message
            print("Video is paused")
            
            
        # key "r" get press
        if symbol == pyglet.window.key.R:
            
            # resume the video
            player.play()
            
            # printing message
            print("Video is resumed")
            
    
            
    # seek video at time stamp = 4
    # and pause the video
    #player.seek(4)
    #player.pause()
    
    # getting texture of the video
    value = player.get_texture()
    
    # printing value of texture
    print("Texture : " + str(value))
            
            
    
    # run the pyglet application
    pyglet.app.run()
    window.close()

#web Browser Settings
chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" 
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))


#Voice Engine Settings
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

wifi_name = "CODER_"

#Functions
def exit_():
    return exit()

def enable_wifi():
    os.system('netsh', 'interface', set , 'interface' +wifi_name+ 'enabled')

def disable_wifi():
    os.system("netsh interface set interface "+wifi_name+" disabled")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email id', 'your email passowrd')
    server.sendmail('your email id', to, content)
    server.close()

def Username():
    speak("What should I call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("Welcome Mr.", uname.center(columns))
   

def devsupport(): 
    b = webbrowser.get('chrome')
    b.open("www.github.com/MIDNIGHT-DEVELOPER")

def sysinfo():
    f = open('systeminfo.txt', 'r+')
    f.truncate(0) # need '0' when using r+
    
    import subprocess
    import sys

    # traverse the info
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []

    # arrange the string into clear info
    for item in Id:
        new.append(str(item.split("\r")[:-1]))
        
    for i in new:
        file_path = 'systeminfo.txt'
        sys.stdout = open(file_path,"a")
        print(i[2:-2])
        
        
        sys.stdout.close()

        #time.sleep(2)
        #with open('systeminfo.txt','r') as firstfile, open('systeminfo_display.txt','a') as secondfile:
      
        # read content from first file
            #for line in firstfile:
               
             # append content to second file
                #secondfile.write(line)
        #os.system(r"systeminfo.txt")
    import subprocess as sp
    programName = "notepad.exe"
    fileName = "systeminfo.txt"
    sp.Popen([programName, fileName])


    def sysinfo():
        
        open(r"D\Project\ZOYA GUI\systeminfo.txt")
    sysinfo()
    



#Quick Buttions 

def Instagram():
    b = webbrowser.get('chrome')
    b.open("https://www.instagram.com/")

def Facebook():
    b = webbrowser.get('chrome')
    b.open("https://www.facebook.com/")

def Twitter():
    b = webbrowser.get('chrome')
    b.open("https://www.twitter.com/")

def Whatsapp():
    b = webbrowser.get('chrome')
    b.open("https://web.whatsapp.com/")

def Gmail():
    b = webbrowser.get('chrome')
    b.open("https://www.gmail.com/")

def Youtube():
    b = webbrowser.get('chrome')
    b.open("https://www.youtube.com/")

def Amazon():
    b = webbrowser.get('chrome')
    b.open("https://www.amazon.com/")

def Flipkart():
    b = webbrowser.get('chrome')
    b.open("https://www.flipkart.com/")


#█ █▀▄▀█ █▀█   █▀▀ █░█ █▄░█ █▀▀ ▀█▀ █ █▀█ █▄░█ █▀
#█ █░▀░█ █▀▀   █▀░ █▄█ █░▀█ █▄▄ ░█░ █ █▄█ █░▀█ ▄█

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Welcome to ZOYA AI Program")
speak("Welcome to ZOYA AI Program")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
        print("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
        print("Good Afternoon Sir!") 

    else:
        speak("Good Evening Sir!")
        print("Good Evening Sir!")

    print("Hi I'm Zoya. Please tell me, How may I help you")
    speak("Hi I'm Zoya. Please tell me, How may I help you")
    
def Features():
    # open method used to open different extension image file
        im = Image.open(r"\Project\ZOYA GUI\Images\AIFeatures.jpg") 
  
        # This method will show image in any image viewer 
        im.show() 

def CovidUpdates():
    b = webbrowser.get('chrome')
    b.open("https://www.covid19india.org/")

def CovidResources():
    import webbrowser
    webbrowser.open(r'file://Project\ZOYA GUI\Files\CovidResources.pdf')
    webbrowser.open(r'file://Project\ZOYA GUI\Files\CovidResources2c.pdf')
    webbrowser.open("https://docs.google.com/spreadsheets/d/1rd8vtTNOkXZ8lxsNW8cYQUBZhtkIIgledPR-md1Oprk/edit#gid=0")

def CovidPrevention():

    import pyglet
 
    # width of window
    width = 1280
    
    # height of window
    height = 720
    
    # caption i.e title of the window
    title = "Covid Preventation"
    
    # creating a window
    window = pyglet.window.Window(width, height, title)
    
    
    # video path
    vidPath ="\\Project\\ZOYA GUI\\Videos\\2.mp4"
    
    # creating a media player object
    player = pyglet.media.Player()
    
    # creating a source object
    source = pyglet.media.StreamingSource()
    
    # load the media from the source
    MediaLoad = pyglet.media.load(vidPath)
    
    # add this media in the queue
    player.queue(MediaLoad)
    
    # play the video
    player.play()
    
    # on draw event
    @window.event
    def on_draw():
        
        # clea the window
        window.clear()
        
        # if player source exist
        # and video format exist
        if player.source and player.source.video_format:
            
            # get the texture of video and
            # make surface to display on the screen
            player.get_texture().blit(0, 0)

    # key press event    
    @window.event
    def on_key_press(symbol, modifier):
    
        # key "p" get press
        if symbol == pyglet.window.key.P:
            
            # pause the video
            player.pause()
            
            # printing message
            print("Video is paused")
            
            
        # key "r" get press
        if symbol == pyglet.window.key.R:
            
            # resume the video
            player.play()
            
            # printing message
            print("Video is resumed")
            
    
            
    # seek video at time stamp = 4
    # and pause the video
    #player.seek(4)
    #player.pause()
    
    # getting texture of the video
    value = player.get_texture()
    
    # printing value of texture
    print("Texture : " + str(value))
            
            
    
    # run the pyglet application
    pyglet.app.run()
    

def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening to you...")
        speak("Listening to you...")
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN' or 'hi-IN')
        print("You said: {}".format(query))
    except Exception as e:
        #print(e)
        print("Try again please.....")
        speak("Try again please.....")
        return "www.google.com"
    query = query.lower()   
    return query



#█▀ ▀█▀ ▄▀█ █▀█ ▀█▀
#▄█ ░█░ █▀█ █▀▄ ░█░


def info():
    messagebox.showinfo("About","I'm your AI Assistant. Developed By Sourabh. Coded in Python.")

def Start():
    
    wishMe()

    while True:

        
        
        query = takeCommand()
        
        assname =("ZOYA")
        
        if 'wikipedia' in query:

            sr.Microphone(device_index=1)
            r=sr.Recognizer()
            r.energy_threshold=5000

            with sr.Microphone() as source:
                audio=r.listen(source)
                try:                   
                    query = query.replace("on wikipedia","")
                    url='https://www.google.co.in/search?q='
                    search_url=url+query
                    b = webbrowser.get('chrome')
                    b.open(search_url)
                except:
                    print("Can't recognize, Please Try again")

            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')

            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            print("According to Wikipedia")
            speak("According to Wikipedia")
            print(results)
            speak(results)

            


            time.sleep(5)

        
        elif 'show me some memories' in query or "do i have memories" in query:
            print("Showing Memories form PC")
            speak("Showing Memories form PC")
            Memories = '\\Project\\ZOYA GUI\\Memories'
            Photos = random.choice(os.listdir(Memories))
            print(Photos)
            os.startfile(os.path.join(Memories, Photos))
            #import PIL
            #import Image

            #filelist = ['test.tif','test2.tif']
            #for imagefile in filelist:
                #im=Image.open(imagefile)
                #box=(50, 50, 200, 200)
                #im_crop=im.crop(box)
                #im_crop.show()

            time.sleep(5)


        elif "what's your name" in query or "what is your name" in query:
            print("My friends call me", assname)
            speak("My friends call me")
            speak(assname)

            time.sleep(5)

        elif 'news' in query:
            
            
            speak("In which language would you like to listen todays top news")
            sr.Microphone(device_index=1)
            r=sr.Recognizer()
            r.energy_threshold=5000

            with sr.Microphone() as source:
                print("Listening...!")
                audio=r.listen(source)
                query=r.recognize_google(audio)
                try:
                    if "English" in query:
                        try:
                            query="todays top news in english"
                            url='https://www.google.co.in/search?q='
                            search_url=url+query
                            b = webbrowser.get('chrome')
                            b.open(search_url)
                        except:
                            print("Can't recognize, Please Try again")

                    elif "Hindi" in query:
                        try:
                            query="todays top news in hindi"
                            url='https://www.google.co.in/search?q='
                            search_url=url+query
                            b = webbrowser.get('chrome')
                            b.open(search_url)
                        except:
                            print("Can't recognize, Please Try again")

                    else:
                        try:
                            query
                            query1="todays top news in "
                            url='https://www.google.co.in/search?q='
                            search_url=url+query1+query
                            b = webbrowser.get('chrome')
                            b.open(search_url)
                        except:
                            print("Can't recognize, Please Try again")
                except:
                            print("Can't recognize, Please Try again")
            time.sleep(5)

        elif ' show system information' in query:
            print("Please wait. Collecting System Information")
            speak("Please wait. Collecting System Information")

            sysinfo()

        elif 'generate random password' in query:
            import random
            import string

            lower = string.ascii_lowercase
            upper = string.ascii_uppercase
            digits = string.digits
            symbol = "@" 


            all = lower + upper + digits + symbol 

            length = 10

            password = "".join(random.sample(all, length))

            print("Random Password is:")
            print(password)

            time.sleep(5)

        elif "open screen recorder" in query:
            import pyautogui
            import cv2
            import numpy as np

            resolution = (1920, 1080)
            codec = cv2.VideoWriter_fourcc(*"XVID")
            filename="ScreenRecording.avi"
            fps=30.0
            out=cv2.VideoWriter(filename , codec , fps ,resolution)
            cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Live",480,270)

            while True:
                img = pyautogui.screenshot()
                frame=np.array(img)
                frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)
                cv2.imshow("Live", frame)

                if cv2.waitKey(1)==ord("q"):
                    break
            out.release()

            cv2.destroyAllWindows()

            time.sleep(5)


        elif 'search' in query:

            try:
                query = query.replace("search","")
                print("You said: {}".format(query))
                url='https://www.google.co.in/search?q='
                search_url=url+query
                b = webbrowser.get('chrome')
                b.open(search_url)
            except:
                    print("Can't recognize, Please Try again")
            time.sleep(5)

        elif 'enable wifi' in query or 'turn-on Wi-Fi' in query:
            print("Enaabling WI-Fi")
            speak("Enaabling WI-Fi")
            os.popen(enable_wifi)

            time.sleep(5)

        elif 'disable wifi' in query or 'turn-off Wi-Fi' in query:
            print("Disabling WI-Fi")
            speak("Disabling WI-Fi")
            os.popen(disable_wifi)

            time.sleep(5)
        
        elif "covid support" in query:
            print('Showing Information')
            speak("Showing Information")
            b = webbrowser.get('chrome')
            b.open("https://www.covid19india.org/")
            b.openr(r'file://Project\ZOYA GUI\Files\CovidResources.pdf')
            b.open("https://docs.google.com/spreadsheets/d/1rd8vtTNOkXZ8lxsNW8cYQUBZhtkIIgledPR-md1Oprk/edit#gid=0")

            time.sleep(5)

        elif "covid prevention" in query:
            print("Playing Video")

            CovidPrevention()

            time.sleep(5)

        elif "dinesh saran" in query:
            b = webbrowser.get('chrome')
            b.open("https://www.facebook.com/PtNrsGovtCollageRohtak/photos/pcb.4513091765474224/4513091688807565/")

        
        elif "dinesh saharan" in query:
            b = webbrowser.get('chrome')
            b.open("https://www.facebook.com/PtNrsGovtCollageRohtak/photos/pcb.4513091765474224/4513091688807565/")


        elif 'youtube' in query:
            b = webbrowser.get('chrome')
            b.open("youtube.com")

            time.sleep(5)

        elif 'twitter' in query:
            b = webbrowser.get('chrome')
            b.open("twitter.com")

            time.sleep(5)

        elif 'google translate' in query:
            b = webbrowser.get('chrome')
            b.open("translate.google.com")

            time.sleep(5)

        elif 'flipkart' in query:
            b = webbrowser.get('chrome')
            b.open("flipkart.com")

            time.sleep(5)

        elif 'pc shop' in query:
            b = webbrowser.get('chrome')
            b.open("pcshop.in")

            time.sleep(5)

        elif 'map' in query:
            b = webbrowser.get('chrome')
            b.open("google.com/maps")

            time.sleep(5)

        elif 'classroom' in query:
            b = webbrowser.get('chrome')
            b.open("https://classroom.google.com/u/1/h")

            time.sleep(5)

        elif 'meet' in query:
            b = webbrowser.get('chrome')
            b.open("meet.google.com/")

            time.sleep(5)

        elif 'discord' in query:
            b = webbrowser.get('chrome')
            b.open("https://discord.com/")

            time.sleep(5)
                                
        elif 'google' in query:
            b = webbrowser.get('chrome')
            b.open("google.com")

            time.sleep(5)

        elif 'instagram' in query:
            b = webbrowser.get('chrome')
            b.open("instagram.com")

            time.sleep(5)

        elif 'search' in query :
            query = query.replace("search", "") 
            b = webbrowser.get('chrome')        
            b.open(query)

            time.sleep(5) 

        elif 'gmail' in query:
            b = webbrowser.get('chrome')
            b.open("gmail.com")

            time.sleep(5)
        
        elif 'github' in query:
            b = webbrowser.get('chrome')
            b.open("github.com")

            time.sleep(5)
        
        elif 'facebook' in query:
            b = webbrowser.get('chrome')
            b.open("facebook.com")

            time.sleep(5)

        elif 'stackoverflow' in query:
            b = webbrowser.get('chrome')
            b.open("stackoverflow.com")

            time.sleep(5)
        
        elif 'whatsapp' in query:
            b = webbrowser.get('chrome')
            b.open("web.whatsapp.com")

            time.sleep(5)

        elif 'yt music' in query:
            b = webbrowser.get('chrome')
            b.open("music.youtube.com")

            time.sleep(5)

        elif 'amazon' in query:
            b = webbrowser.get('chrome')
            b.open("amazon.in")

            time.sleep(5)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")

            time.sleep(5)
            
        elif 'code' in query:
            Path = "C:\\Users\\didio\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Path)  

            time.sleep(5)
        
        elif 'chrome' in query:
            Path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            os.startfile(Path)

            time.sleep(5)

        elif 'virtual dj' in query:
            Path = 'C:\\Program Files\\VirtualDJ\\virtualdj.exe'
            os.startfile(Path)

            time.sleep(5)
        
        elif 'torrent' in query:
            Path = "C:\\Users\\didio\\AppData\\Roaming\\uTorrent\\uTorrent.exe"
            os.startfile(Path)

            time.sleep(5)

        elif 'edge' in query:
            Path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(Path)

            time.sleep(5)
        
        elif 'explorer' in query:
            Path = "C:\\Windows\\explorer.exe"
            os.startfile(Path)

            time.sleep(5) 

        elif 'games folder' in query:
            Path = "D:\\Games"
            os.startfile(Path)

            time.sleep(5)

        elif 'downloads folder' in query:
            Path = "C:\\Users\\didio\\Downloads"
            os.startfile(Path)

            time.sleep(5)

        
        elif 'music folder' in query:
            Path = "C:\\Users\\didio\\Music"
            os.startfile(Path)

            time.sleep(5)

        elif 'videos folder' in query:
            Path = "C:\\Users\\didio\\Videos"
            os.startfile(Path)

            time.sleep(5)
            
        elif 'notepad plus' in query:
            Path = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(Path)

            time.sleep(5)
                
        elif 'calculator' in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')

            time.sleep(5)

        elif 'camera' in query:
            subprocess.run('start microsoft.windows.camera:', shell=True)

            time.sleep(5)
        
        elif 'notepad' in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

            time.sleep(5)

        elif 'wordpad' in query:
            subprocess.Popen('C:\\Windows\\System32\\write.exe')

            time.sleep(5)

        elif 'task manager' in query:
            subprocess.Popen('C:\\Windows\\System32\\taskmgr.exe')

            time.sleep(5)

        elif 'command' in query:
            subprocess.Popen('C:\\Windows\\System32\\cmd.exe')

            time.sleep(5)

        elif 'ms info' in query:
            subprocess.Popen('C:\\Windows\\System32\\msinfo32.exe')

            time.sleep(5)

        elif 'dialer' in query:
            subprocess.Popen('C:\\Windows\\System32\\dialer.exe')

            time.sleep(5)

        elif 'snipping tool' in query:
            subprocess.Popen('C:\\Windows\\System32\\SnippingTool.exe')

            time.sleep(5)

        elif 'resource manager' in query:
            subprocess.Popen('C:\\Windows\\System32\\resmon.exe')

            time.sleep(5)

        elif 'performance manager' in query:
            subprocess.Popen('C:\\Windows\\System32\\perfmon.exe')

            time.sleep(5)

        elif 'ms config' in query:
            subprocess.Popen('C:\\Windows\\System32\\msconfig.exe')

            time.sleep(5)

        elif 'dx diag' in query:
            subprocess.Popen('C:\\Windows\\System32\\dxdiag.exe')

            time.sleep(5)

        elif 'device properties' in query:
            subprocess.Popen('C:\\Windows\\System32\\DeviceProperties.exe')

            time.sleep(5)

        elif 'game panel' in query:
            subprocess.Popen('C:\\Windows\\System32\\GamePanel.exe')

            time.sleep(5)

        elif 'paint' in query:
            subprocess.Popen('C:\\Windows\\System32\\mspaint.exe')

            time.sleep(5)

        elif "check internet speed" in query:
            b = webbrowser.get('chrome')
            b.open("https//www.fast.com")

        
        elif "local disk a" in query: 
            try:
                os.startfile("A:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("A:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk b" in query: 
            try:
                os.startfile("B:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("B:")
                print("Disk Not Found")
                speak("Disk Not Found")


            time.sleep(5)

        elif "local disk c" in query: 
            try:
                os.startfile("C:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("C:")
                print("Disk Not Found")
                speak("Disk Not Found")


            time.sleep(5)

        elif "local disk d" in query: 
            try:
                os.startfile("D:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("D:")
                print("Disk Not Found")
                speak("Disk Not Found")


            time.sleep(5)

        elif "local disk e" in query: 
            try:
                os.startfile("E:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("E:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)
        
        elif "local disk f" in query: 
            try:
                os.startfile("F:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("F:")
                print("Disk Not Found")
                speak("Disk Not Found")


            time.sleep(5)
        
        elif "local disk g" in query: 
            try:
                os.startfile("G:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists(":G")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk h" in query: 
            try:
                os.startfile("H:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("H:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk i" in query: 
            try:
                os.startfile("I:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("I:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk j" in query: 
            try:
                os.startfile("J:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("J:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk k" in query: 
            try:
                os.startfile("K:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("K:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk l" in query: 
            try:
                os.startfile("L:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("L:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk m" in query: 
            try:
                os.startfile("M:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("M:")
                print("Disk Not Found")


            time.sleep(5)

        elif "local disk n" in query: 
            try:
                os.startfile("N:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("N:")
                print("Disk Not Found")

            time.sleep(5)
        
        elif "local disk o" in query: 
            try:
                os.startfile("O:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("O:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk p" in query: 
            try:
                os.startfile("P:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("P:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk q" in query: 
            try:
                os.startfile("Q:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("Q:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk r" in query: 
            try:
                os.startfile("R:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("R:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk s" in query: 
            try:
                os.startfile("S:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("S:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)
        
        elif "local disk t" in query: 
            try:
                os.startfile("T:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("T:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk u" in query: 
            try:
                os.startfile("U:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("U:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk v" in query: 
            try:
                os.startfile(":V")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("V:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)

        elif "local disk w" in query: 
            try:
                os.startfile("W:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("W:")
                print("Disk Not Found")
                speak("Disk Not Found")

            time.sleep(5)
        
        elif "local disk x" in query: 
            try:
                os.startfile("X:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("X:")
                print("Disk Not Found")
                speak("Disk Not Found")
            time.sleep(5)

        elif "local disk y" in query: 
            try:
                os.startfile("Y:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("Y:")
                print("Disk Not Found")
                speak("Disk Not Found")
            time.sleep(5)

        elif "local disk z" in query: 
            try:
                os.startfile("Z:")
                print("Opening Disk")
                speak("Opening Disk")
            except Exception as e:
                not os.path.exists("Z:")
                print("Disk Not Found")
                speak("Disk Not Found")
            time.sleep(5)
        
        elif 'set reminder' in query:
            print("What shall I remind you about?")
            text = str(input())
            print("In how many minutes?")
            local_time = float(input())
            local_time = local_time * 60
            time.sleep(local_time)
            print(text)

            time.sleep(5)

        elif 'play music' in query:
            import random

            speak("Playing Music from PC")
            print("Playing Music from PC")
            music_dir = '\\Project\\ZOYA GUI\\Music'
            songs = random.choice(os.listdir(music_dir))
            print(songs)
            os.startfile(os.path.join(music_dir, songs))

            time.sleep(5)

        elif "open presentation" in query:
            print("Opening Your File")
            speak("Opening Your File")

            import subprocess as sp
            programName = r"C:\Users\\AppData\Local\Kingsoft\WPS Office\11.2.0.10382\office6\WPS.exe"
            fileName = (r"\Project\ZOYA GUI\Files\Presentation.pptx")
            sp.Popen([programName, fileName])

        elif 'about you' and "apne bare me" in query:
            query = query.replace("about you" and "apne bare me","")   
            print('I an an AI Assistant. Developed by Sourabh. Coded in Python' )
            speak('I an an AI Assistant. Developed by Sourabh. Coded in Python' )

            time.sleep(5)
            
        elif "good morning" in query:
                speak("A warm" + query)
                print("How are you Coder?")
                speak("How are you Coder?")

                time.sleep(5)   
            
                
        elif "good afternoon" in query:
                speak("A warm" + query)
                print("How are you Coder?")
                speak("How are you Coder?")
                
                time.sleep(5)
        
        elif "good evening" in query:
                speak("A warm" + query)
                print("How are you Coder?")
                speak("How are you Coder?")
                
                time.sleep(5)
        
        elif "good night" in query:
                speak("A warm" + query)
                print("How are you Coder?")
                speak("How are you Coder?")
                
                time.sleep(5)

        elif 'send a mail' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    speak("To whom should i send")
                    to = input()    
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

                time.sleep(5)

        elif "will you be my gf" in query:   
                speak("I'm not sure about, may be you should give me some time")

                time.sleep(5)

        elif "how are you" in query:
                speak("I'm fine, glad you ask me that")

                time.sleep(5)

        elif "i love you" in query:
                speak("Sorry I'm love with your wifi")

                time.sleep(5)

        elif "write a note" in query:
                speak("What should i write, sir")
                note = takeCommand()
                file = open('Notpad.txt', 'a')
                print("Should I include date and time")
                speak("Should I include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(":-")
                    file.write(note)
                else:
                    file.write(note)

                time.sleep(5)
            
        elif "show note" in query:
                speak("Showing Notes")
                file = open("Notpad.txt", "r") 
                print(file.read())
                speak(file.read(6))

                time.sleep(5)

        elif 'how are you?' in query:
                speak("I am fine, Thanks for asking :)")
                print("I am fine, Thanks for asking :)")
                speak("How are you, Sir")

                if 'fine' in query or "good" in query:
                    speak("It's good to know that you're fine")

                time.sleep(5)

        elif "change my name to" in query:
                query = query.replace("change my name to", "")
                assname = query

                time.sleep(5)

        elif "change name" in query:
                speak("What would you like to call me, Sir ")
                assname = takeCommand()
                speak("Thanks for naming me")

                time.sleep(5)

        elif "what's your name" in query or "What is your name" in query:
                speak("My friends call me")
                speak(assname)
                print("My friends call me", assname)

                time.sleep(5)

        elif "who made you" in query or "who created you" in query: 
            print("I have been created by CODER.")
            speak("I have been created by CODER.")

            time.sleep(5)

        elif "who i am" in query:
            speak("If you talk then definately your human.")
            print("If you talk then definately your human.")

            time.sleep(5)

        elif "why you came to world" in query:
            speak("Thanks to Coder further it's a secret")
            print("Thanks to Coder further it's a secret")

            time.sleep(5)

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
            print("It is 7th sense that destroy all other senses")

            time.sleep(5)

        elif "who are you" in query:
            speak("I'm ZOYA, your virtual assistant")
            print("I'm ZOYA, your virtual assistant")

            time.sleep(5)

        elif 'reason for you' in query:
            print("To help you dear.")
            speak("To help you dear.")

            time.sleep(5)
            
                    
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            print("Recycle Bin Cleaned")
            speak("Recycle Bin Cleaned")

            time.sleep(5)

        elif "don't listen" in query or "stop listening" in query:
            print("For how much time you want to stop ZOYA from listening commands")
            speak("For how much time you want to stop ZOYA from listening commands")
            a = StringVar(takeCommand())
            time.sleep(a)
            print(a)

            time.sleep(5)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

            time.sleep(5)

        elif "scan for open ports" in query:
            print("Scaning for Open Ports on your device.")
            speak("Scaning for Open Ports on your device.")

            import socket  #importing library 
            import pyfiglet 
            import sys
            from datetime import datetime

            ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
            print(ascii_banner)

            target = socket.gethostbyname(socket.gethostname())

            print("-" * 50)
            print("Scanning Target: " + target)
            print("Scanning started at:" + str(datetime.now()))
            print("-" * 50)
  
            ip = socket.gethostbyname (socket.gethostname())  #getting ip-address of host
  
            for port in range(65535):      #check for all available ports
  
                try:
   
                    serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # create a new socket
  
                    serv.bind((ip,port)) # bind socket with address
             
                except:
  
                    print('[OPEN] Port open :',port) #print open port number
  
            serv.close() #close connection

            print("Some Ports Can Compromise With Your Device Security")
            speak("Some Ports Can Compromise With Your Device Security")
            time.sleep(2)
            print("You Can Turn Some Unused Ports Manually Using This Manual")
            speak("You Can Turn Some Unused Ports Manually Using This Manual")

            ########
            #Using PIL module to open Photos
    
            # open method used to open different extension image file
            im = Image.open(r"\Project\ZOYA GUI\Images\CommonPorts.jpg") 
  
            # This method will show image in any image viewer 
            im.show() 

            time.sleep(10)

#Power Realated Commands

        elif 'lock window' in query:
                print("locking the device")
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

                time.sleep(5)

        elif 'shutdown system' in query:
                print("Hold On ! Your system is on its way to shut down. Make sure you have you've saved you work")
                speak("Hold On ! Your system is on its way to shut down. Make sure you have you've saved you work")
                time.sleep(10)
                subprocess.call('shutdown / p /f')

                time.sleep(5)

        elif "restart" in query:
            print("Make sure all the application are closed and saved before restarting.")
            speak("Make sure all the application are closed and saved before restarting.")
            print("Window will restart within 5 seconds.")
            time.sleep(5)
            subprocess.call(["shutdown", "/r"])

            time.sleep(5)
                
        elif "hibernate" in query: 
            print("Hibernating")
            speak("Hibernating")
            subprocess.call("shutdown /h")

            time.sleep(5)
            

        elif "sleep" in query:
            print("Window will sleep within 5 seconds.")
            speak("Window will sleep within 5 seconds.")

            time.sleep(5)
            
            time.sleep(5)
            print("Sleeping")
            speak("Sleeping")
            subprocess.call("shutdown /h")

            time.sleep(5)

        elif "log off" in query or "sign out" in query:
            print("Make sure all the application are closed before sign-out.")
            speak("Make sure all the application are closed before sign-out")
            print("Window will Log-off within 5 seconds.")
            
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "exit" in query or "quit" in query:
            print("Ok, Sure")
            speak("Ok, Sure")
            time.sleep(1)
            print("See You Soon Dear")
            speak("See You Soon Dear")
            print("Exiting..")
            exit_()

            

        elif "You can sleep " in query or "sleep now " in query:
            print("Ok sir, I'm going to sleep now you can call me anytime")
            speak("Ok sir, I'm going to sleep now you can call me anytime")
            break

            
        else:              
            sr.Microphone(device_index=1)
            r=sr.Recognizer()
            r.energy_threshold=5000

            with sr.Microphone() as source:
                audio=r.listen(source)
                try:                   
                    query
                    url='https://www.google.co.in/search?q='
                    search_url=url+query
                    b = webbrowser.get('chrome')
                    b.open(search_url)
                except:
                    print("Can't recognize, Please Try again")


            time.sleep(3)

#def send():
#    print("OK")
    

canvas_width = 900
canvas_height = 500  



root =Tk()
root.title("ZOYA version 2.0")

root.geometry("900x600")
root.minsize(900,600)
root.maxsize(900,600)

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

can_widget.create_line(450, 0, 450, 500, fill="red")

L1= Label(text="ZOYA AI" , fg="Black", font="Aquarilla 40 ", relief=SUNKEN)
L1.pack()
L1.place(x=170,y=0)

L2= Label(text="ZOYA ver 2.0", bg="white" ,fg="Black", font="Voltec 10 " )
L2.pack(side=BOTTOM , anchor="sw")

L3= Label( text="COVID-19 Support", bg="white" , fg="black", font="Voltec 10 ")
L3.pack()
L3.place(x=620,y=510)

L4= Label( text="Quick Buttons", bg="white" , fg="black", font="Voltec 10 ")
L4.pack()
L4.place(x=185,y=510)


#L3= Label(text="Next", fg="Cyan", font="Bilbo 10 bold", relief=SUNKEN)
#L3.pack()

#L4= Label(text="Exit", fg="Cyan", font="Bilbo 10 bold", relief=SUNKEN)
#L4.pack()

#L5= Label(text="Show Info", fg="Cyan", font="Bilbo 10 bold", relief=SUNKEN)
#L5.pack(anchor=CENTER)

#L0= Frame(text="About", fg="Black", font="Bilbo 10 bold", relief=SUNKEN)
#L0.pack(side=BOTTOM , anchor="ne")



#Buttons Frames

F0= Frame(root, borderwidth=10 , bg="Black", relief=SUNKEN )
F0.pack(side=BOTTOM , anchor=CENTER)
F0.place(x=730 ,y=00)

F1= Frame(root, borderwidth=50 , bg="black" , relief=SUNKEN)
F1.pack(side=TOP , anchor=CENTER)
F1.place(x=130 ,y=160)

F2= Frame(root, borderwidth=10 , bg="black" , relief=SUNKEN ,  width="12", height="5")
F2.pack(side=BOTTOM , anchor=CENTER)
F2.place(x=20,y=530)

F3= Frame(root, borderwidth=10 , bg="black" , relief=SUNKEN ,  width="12", height="5")
F3.pack(side=BOTTOM , anchor=CENTER)
F3.place(x=470,y=530)

#Main Control Buttons 

b1=Button(F1,text="Start",bg="Black", fg="White" ,command=Start)
b1.pack(side=TOP)

b2=Button(F1,text="Exit",bg="Black", fg="White" ,command=exit_)
b2.pack(side=BOTTOM)

b3=Button(F1,text="Show Info",bg="Black" , fg="White" ,command=info)
b3.pack(side=BOTTOM)

b4=Button(F1,text="Features",bg="Black" , fg="White" ,font="Arial 10 ",command=Features)
b4.pack()

b5=Button(F1,text="Click To Play",bg="Black" , fg="White" ,font="Arial 10 ",command=SelfIntro)
b5.pack()

#Covid Rresources

b1=Button(F3,text="COVID-19 Updates",bg="Black" , fg="White" ,font="Arial 10 ",command=CovidUpdates)
b1.pack(side=LEFT)

b2=Button(F3,text="COVID-19 Resources",bg="Black" , fg="White" ,font="Arial 10 ",command=CovidResources)
b2.pack(side=LEFT)

b3=Button(F3,text="COVID-19 Prevention",bg="Black" , fg="White" ,font="Arial 10 ",command=CovidPrevention)
b3.pack(side=LEFT)


#Bottom Left Buttons

b1=Button(F0,text="Support",bg="Black" , fg="White" ,font="Arial 9 ",command=devsupport)
b1.pack(side=LEFT)

b2=Button(F0,text="System Info",bg="Black" , fg="White" ,font="Arial 9 ",command=sysinfo)
b2.pack(side=LEFT)


#Social Media Link

b1=Button(F2,text="Instagram",bg="Black", fg="White" , font="Arial 8" ,command=Instagram)
b1.pack(side=LEFT)

b2=Button(F2,text="Facebook",bg="Black", fg="White", font="Arial 8" ,command=Facebook)
b2.pack(side=LEFT)

b3=Button(F2,text="Twitter",bg="Black" , fg="White", font="Arial 8" , command=Twitter)
b3.pack(side=LEFT)

b4=Button(F2,text="Gmail",bg="Black" , fg="White" ,font="Arial 8",command=Gmail)
b4.pack(side=LEFT)

b5=Button(F2,text="Youtube",bg="Black" , fg="White" ,font="Arial 8",command=Youtube)
b5.pack(side=LEFT)

b6=Button(F2,text="Whatsapp",bg="Black" , fg="White" ,font="Arial 8",command=Whatsapp)
b6.pack(side=LEFT)

b7=Button(F2,text="Amazon",bg="Black" , fg="White" ,font="Arial 8",command=Amazon)
b7.pack(side=LEFT)

b8=Button(F2,text="Flipkart",bg="Black" , fg="White" ,font="Arial 8",command=Flipkart)
b8.pack(side=LEFT)




#ChatLog = Text(root, bd=0, bg="Black", height="8", width="50", font="Arial",)

#ChatLog.config(state=NORMAL)

#Bind scrollbar to Chat window
#scrollbar = Scrollbar(root, bg="Black" ,command=ChatLog.yview, cursor="heart")
#ChatLog['yscrollcommand'] = scrollbar.set
#ChatLog.update

#Create Button to send query
#EnterButton = Button(root, font=("Pristina",12,'bold'),bg="Black", text="Enter", width="12", height=5,
#                    bd=0, activebackground="#3c9d9b",fg='#ffffff',
#                    command= send )
#EnterButton.pack

#Create the box to enter message
#box1 = Text(root, bd=0, bg="White",width="29", height="5", font="Arial")
#box1.pack()

#box1.bind("<Return>", send)

#Place all components on the screen
#scrollbar.place(x=870,y=50, height=500)
#ChatLog.place(x=500,y=50, height=500, width=370)
#box1.place(x=620, y=555, height=30, width=265)
#EnterButton.place(x=500, y=555, height=30)

#Logo CODE
photo = PhotoImage(file =r"\Project\ZOYA GUI\Images\AI logo.png")
root.iconphoto(False, photo)
  



#GIF
frameCnt = 50
frames = [PhotoImage(file=r'\Project\ZOYA GUI\Images\giphy.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)
label.pack()
label.place(x=470,y=55, height=450, width=410)
root.after(0, update, 0)

#TransparentUIEffect
#root.attributes('-alpha',0.8)


root.mainloop()
