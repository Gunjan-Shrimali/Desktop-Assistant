from tkinter import *
from PIL import Image,ImageTk      #for creating an background wallpaper
import tkinter as tk
#from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import Menu
from time import strftime 
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import mysql.connector


window = Tk()

window.title("SEARCH@gs_ANYTHING HERE")
window.geometry('1250x500') # ('colxrow')

#txt = scrolledtext.ScrolledText(window, width=40, height=10)

#txt.grid(column=25, row=100)

lbl = Label (window, text="SearchWithGunu", font=("Times new Roman", 40))

lbl.grid(column=25, row=25)
#------entry box for search -----


txt = Entry(window, width=60)

txt.grid(column=25, row=50)

#---- AI code ----

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    
    speak("I am Mini Gunjan Sir. Please tell me how may I help you")
    speak("What is your name ?")
def nameCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
        print("Say that again please...")  
        return "None"
    return query


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
#--------


def clicked():
      if __name__ == "__main__":
            wishMe()
            while True:
                  query = nameCommand().lower()

        # Logic for executing tasks based on query
                  if 'my name is' in query:
                        
              
                        #speak('Searching Wikipedia...')
                        query = query.replace("my name is", "")
                        #results = wikipedia.summary(query, sentences=2)
                        #speak("According to Wikipedia")
                        #print(query)
                        speak("ok ")
                        speak(query)
                        speak("what may i help you")
                  elif 'open youtube' in query:
                        webbrowser.open("youtube.com")
          # if 1:
                  query = takeCommand().lower()
        
          # Logic for executing tasks based on query
                  if 'wikipedia' in query:
        
                        speak('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
            

                  elif 'open youtube' in query:
                              webbrowser.open("youtube.com")
            
                  elif 'open mpg programming' in query:
                              webbrowser.open("https://www.youtube.com/watch?v=3Eo3xfHlOj8")

                  elif 'open google' in query:
                              webbrowser.open("google.com")

                  elif 'open stackoverflow' in query:
                              webbrowser.open("stackoverflow.com")   


                  elif 'play music' in query:
                              music_dir = 'E:\my fav song'
                              songs = os.listdir(music_dir)
                              print(songs)    
                              os.startfile(os.path.join(music_dir, songs[0]))

                  elif 'the time' in query:
                              strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                              speak(f"Sir, the time is {strTime}")

                  elif 'open code' in query:
                              codePath = "E:\DOCUMENTS\gunjan_desktop assistant"
                              os.startfile(codePath)

                  elif 'email to gunjan' in query:
                              try:
                                    
                                    speak("What should I say?")
                                    content = takeCommand()
                                    to = "gunjanshrimali407@gmail.com"    
                                    sendEmail(to, content)
                                    speak("Email has been sent!")
                              except Exception as e:
                                    print(e)
                              speak("Sorry my friend gunjan bhai. I am not able to send this email")
def search():
    a_website = txt.get()#"https://www.google.com"
    
 
# Open url in a new window of the default browser, if possible
    webbrowser.open_new(a_website)
 
# Open url in a new page (“tab”) of the default browser, if possible
    #webbrowser.open_new_tab(a_website)
 
    #webbrowser.open(a_website, 1) # Equivalent to: webbrowser.open_new(a_website)
    #webbrowser.open(a_website, 2) # Equivalent to: webbrowser.open_new_tab(a_website)
def camera():
     webbrowser.open("https://turncameraon.com/#")

#--------------------search button ---------------------------

# Creating a photoimage object to use image 
photo99 = PhotoImage(file = r"C:\mr\find.png") 

# Resizing image to fit on button 
photoimage99 = photo99.subsample(3,3) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button   
btn = Button(window, text="",image=photoimage99,compound = LEFT ,command=search)

btn.grid(column=25, row=75)

#-------------------creating Mike_button With image---------------------

# Creating a photoimage object to use image 
photo = PhotoImage(file = r"C:\mr\gunu.png") 

# Resizing image to fit on button 
photoimage = photo.subsample(15,15) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn2=Button(window, text = '', image = photoimage, 
					compound = LEFT,command=clicked) 
btn2.grid(column=30,row=50)
#-------------------creating camera_button With image---------------------

# Creating a photoimage object to use image 
photo51 = PhotoImage(file = r"C:\mr\camera.png") 

# Resizing image to fit on button 
photoimage51 = photo51.subsample(6,6) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn51=Button(window, text = '', image = photoimage51, 
					compound = LEFT,command=camera) 
btn51.grid(column=31,row=50)
#mainloop()
#-------------------background image -----------------

IMAGE_PATH = 'insta.png'
WIDTH, HEIGTH = 1250, 500
canvas = tk.Canvas(window, width=WIDTH, height=HEIGTH)
#canvas.pack()
img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)
#window.mainloop()

#-------------------creating shorcut------------------
#----shortcut(1)------

def aditi():
    webbrowser.open("https://www.youtube.com/watch?v=3Eo3xfHlOj8")
# Creating a photoimage object to use image 
photo1 = PhotoImage(file = r"C:\mr\mpg.png") 

# Resizing image to fit on button 
photoimage1 = photo1.subsample(18,18) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn3=Button(window, text = '', image = photoimage1, 
					compound = LEFT,command=aditi) 
btn3.grid(column=5,row=401)
#-----shortcut(2)--------
def usha():
    webbrowser.open("https://www.google.com/gmail")
photo2 = PhotoImage(file = r"C:\mr\gmail.png") 

# Resizing image to fit on button 
photoimage2 = photo2.subsample(15,15) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn3=Button(window, text = '', image = photoimage2, 
					compound = LEFT,command=usha) 
btn3.grid(column=31,row=401)
#-----shortcut(3)---------
def bhumika():
    webbrowser.open("https://www.youtube.com/")
photo3 = PhotoImage(file = r"C:\mr\youtube.png") 

# Resizing image to fit on button 
photoimage3 = photo3.subsample(10,10) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn4=Button(window, text = '', image = photoimage3, 
					compound = LEFT,command=bhumika) 
btn4.grid(column=30,row=401)
#-----shortcut(4)--------
def ram():
    webbrowser.open("https://www.instagram.com/")
photo4 = PhotoImage(file = r"C:\mr\insta.png") 

# Resizing image to fit on button 
photoimage4 = photo4.subsample(15,15) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn5=Button(window, text = '', image = photoimage4, 
					compound = LEFT,command=bhumika) 
btn5.grid(column=15,row=401)
#-----shortcut(5)--------
def face():
    webbrowser.open("https://www.facebook.com/")
photo5 = PhotoImage(file = r"C:\mr\fb.png") 

# Resizing image to fit on button 
photoimage5 = photo5.subsample(7,7) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn5=Button(window, text = '', image = photoimage5, 
					compound = LEFT,command=face) 
btn5.grid(column=16,row=401)
#------shortcut(6)---------
def twitter():
    webbrowser.open("https://www.twitter.com/")
photo6 = PhotoImage(file = r"C:\mr\twitter.png") 

# Resizing image to fit on button 
photoimage6 = photo6.subsample(4,4) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn6=Button(window, text = '', image = photoimage6, 
					compound = LEFT,command=twitter) 
btn6.grid(column=17,row=401)
#------shourtcut(7)----------
def tiktok():
    webbrowser.open("https://www.tiktok.com/")
photo7 = PhotoImage(file = r"C:\mr\tiktok.png") 

# Resizing image to fit on button 
photoimage7 = photo7.subsample(12,14) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn7=Button(window, text = '', image = photoimage7, 
					compound = LEFT,command=tiktok) 
btn7.grid(column=18,row=401)
#---------shortcut(8)----------
def amazon():
    webbrowser.open("https://www.amazon.com/")
photo8 = PhotoImage(file = r"C:\mr\amazon.png") 

# Resizing image to fit on button 
photoimage8 = photo8.subsample(10,10) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn8=Button(window, text = '', image = photoimage8, 
					compound = LEFT,command=amazon) 
btn8.grid(column=19,row=401)
#---------shortcut(9)---------
def whats():
    webbrowser.open("https://www.whatsapp.com/")
photo9 = PhotoImage(file = r"C:\mr\gb1.png") 

# Resizing image to fit on button 
photoimage9 = photo9.subsample(4,4) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn9=Button(window, text = '', image = photoimage9, 
					compound = LEFT,command=whats) 
btn9.grid(column=24,row=401)
#---------shortcut(10)---------
def linkn():
    webbrowser.open("https://in.linkedin.com/")
photo10 = PhotoImage(file = r"C:\mr\link.png") 

# Resizing image to fit on button 
photoimage10 = photo10.subsample(4,4) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn10=Button(window, text = '', image = photoimage10, 
					compound = LEFT,command=linkn) 
btn10.grid(column=34,row=401)
#---------shortcut(11)----------
def india():
    webbrowser.open("https://india.gov.in/")
photo11 = PhotoImage(file = r"C:\mr\india.png") 

# Resizing image to fit on button 
photoimage11 = photo11.subsample(4,6) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn11=Button(window, text = '', image = photoimage11, 
					compound = LEFT,command=india) 
btn11.grid(column=32,row=401)
#---------shortcut(11)----------
def java():
    webbrowser.open("https://java.com/")
photo12 = PhotoImage(file = r"C:\mr\java1.png") 

# Resizing image to fit on button 
photoimage12 = photo12.subsample(4,4) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn12=Button(window, text = '', image = photoimage12, 
					compound = LEFT,command=java) 
btn12.grid(column=33,row=401)
#---------shortcut(12)----------
def rtu():
    webbrowser.open("https://rtu.ac.in/")
photo13 = PhotoImage(file = r"C:\mr\rtu.png") 

# Resizing image to fit on button 
photoimage13 = photo13.subsample(6,6) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn13=Button(window, text = '', image = photoimage13, 
					compound = LEFT,command=rtu) 
btn13.grid(column=35,row=401)
#--------------------creating login button------------------------
def data():
    
    window=Tk()
    window.title("LOGIN FORM")
    window.geometry('500x300')

#txt = scrolledtext.ScrolledText(window, width=40, height=10)

#txt.grid(column=25, row=100)

    lbl101 = Label (window, text="LOGIN FORM", font=("Times new Roman", 16))
    lbl101.grid(column=50, row=25)

    lbl102 = Label (window, text='NAME', font=("times new roman",11))
    lbl102.grid(column=25 , row=50)

         
    txt101 = Entry(window, width=50)

    txt101.grid(column=50, row=50)

    lbl104 = Label (window,text='EMAIL', font=("times new roman",11))
    lbl104.grid(column=25 , row=100)

    lb105 = Label (window,text='PASSWORD', font=("time new roman",11))
    lb105.grid(column=25 , row=150)

    txt104 = Entry(window,width=50)
    txt104.grid(column=50,row=100)

    txt105 = Entry(window,width=50)
    txt105.grid(column=50,row=150)

    a=txt101.get()
    b=txt104.get()
    c=txt105.get()


    def clicked():
        mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='9521',
        database='db1'
        )
        cur=mydb.cursor()
        s="INSERT INTO student (NAME,EMAIL,PASSWORD) VALUES(%s,%s,%s)"
        b1=(a,b,c)     #using tuple we put values into the format cb
        cur.execute(s,b1)
       #cur.execute(s,2,b)
       #cur.execute(s,3,c)
        mydb.commit()
        print("SUCESS: RECORD SAVED SUCESSFULYY")
#    lbl.configure(text="Request is Applied  !!",font=("Times new Roman",10))
#   lbl.grid(column=10,row=75)

    btn110 = Button(window, text="LOGIN", bg='White', fg='Black',command=clicked)

    btn110.grid(column=50, row=200)

    btn111 = Button(window, text="RESET",bg='white', fg='Black')

    btn111.grid(column=52,row=200)


    window.mainloop()

    
photo14 = PhotoImage(file = r"C:\mr\acc.png") 

# Resizing image to fit on button 
photoimage14 = photo14.subsample(22,22) 

# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btn14=Button(window, text = '', image = photoimage14, 
					compound = LEFT,command=data) 
btn14.grid(column=37,row=25)


#--------------------creating watch on the gui--------------------------
def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 
  
# Styling the label widget so that clock 
# will look more attractive 
lbl = Label(window, font = ('calibri', 40, 'bold'), 
            background = 'black', 
            foreground = 'white') 
  
# Placing clock at the centre 
# of the tkinter window 
lbl.grid(column=25,row=401) 
time()

menu = Menu(window)

new_item = Menu(menu)
new_item1 = Menu(menu)
new_item2 = Menu(menu)
new_item3 = Menu(menu)

new_item.add_command(label='Images')
new_item.add_separator()
new_item.add_command(label='HIstroy')
new_item.add_separator()
new_item.add_command(label='new_ignotic tab')
new_item.add_separator()
new_item.add_command(label='help')
new_item.add_separator()
new_item.add_command(label='more tools')
new_item.add_separator()
new_item.add_command(label='Zoom - & +')
new_item.add_separator()
new_item.add_command(label='setting')
new_item.add_separator()
new_item.add_command(label='Exit')
new_item.add_separator()
new_item1.add_command(label='version 1.0')
new_item1.add_separator()
new_item2.add_command(label='MY GUNU IMAGE')
new_item2.add_separator()
new_item2.add_command(label='MY GUNU TUBE')
new_item2.add_separator()
new_item2.add_command(label='MPG PROGRAMMING')
new_item2.add_separator()
new_item3.add_command(label='gunjanshrimali1234@gmail.com')
new_item3.add_separator()
new_item3.add_command(label='gunjanshrimali407@gmail.com')
new_item3.add_separator()
new_item3.add_command(label='mpgsite09@gmail.com')

menu.add_cascade(label='Menu', menu=new_item)
menu.add_cascade(label='Gmail', menu=new_item3)
menu.add_cascade(label='GUNJAN APP', menu=new_item2)
menu.add_cascade(label='SIGN UP', menu=new_item1)


window.config(menu=menu)

window.mainloop()
