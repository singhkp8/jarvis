import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import os
import pyjokes
import cv2
import winsound
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis sir What Can I do For You")

def takeCommand():

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
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourgmail', 'your password')
    server.sendmail('singhkavyapal@gmail.com', to,subject, content)
    server.close()

def SecurityCamera():
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret,frame1 = cam.read()
        ret,frame2 = cam.read()
        diff = cv2.absdiff(frame1 , frame2)
        gray = cv2.cvtColor(diff , cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh , None , iterations=3)
        contours, _ = cv2.findContours(dilated , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame1 , contours, -1 , (0 , 255 , 0) , 2)
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame1 , (x , y) , (x + w , y + h) , (0 , 255 , 0) , 2)
            winsound.Beep(500,100)
        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow('kavya cam' , frame1)


if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'hello' in query:
            speak("Hello sir How are you ")

        elif 'fine' in query:
            speak("that great sir please tell me what can i do")

        # elif 'google ' in query:
        #     speak("what should i search")
        #     # whatwouldsearch = takeCommand()
        #     # speak('searching ' + whatwouldsearch)
        #     pywhatkit.search(whatwouldsearch)

        elif 'play' in query:
            whatShouldPlay = query.replace('play', '')
            speak('playing ' + whatShouldPlay)
            pywhatkit.playonyt(whatShouldPlay)


        elif 'open code' in query :
            codePath = "C:\\Users\\singhk3\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'quit' in query:
            speak("Bye Sir Have A Nice Day.")
            speak("If You Want More Help Please call Me Again.")
            speak("Thanks")
            exit()

        elif 'camera' in query:
            SecurityCamera()

        elif 'open boost' in query:
            webbrowser.open("boostcrm.lightning.force.com")

        elif 'open citibank' in query:
            webbrowser.open(".citibank.co.in/ibank/login/IQPin1.jsp?dOfferCode=PAYCCBILL")

        elif 'open ss' in query:
            webbrowser.open("training.sharesource.com/group/train-05")

        elif '2016' in query :
            codePath = "C:\\Users\\singhk3\\Desktop\\Baxter\\2016"
            os.startfile(codePath)

        elif '2017' in query :
            codePath = "C:\\Users\\singhk3\\Desktop\\Baxter\\2017"
            os.startfile(codePath)

        elif '2018' in query :
            codePath = "C:\\Users\\singhk3\\Desktop\\Baxter\\2018"
            os.startfile(codePath)
        elif '2019' in query :
            codePath = "C:\\Users\\singhk3\\Desktop\\Baxter\\2019"
            os.startfile(codePath)

        elif '2020' in query :
            codePath = "C:\\Users\\singhk3\\Desktop\\Baxter\\2020"
            os.startfile(codePath)

        elif 'baxter' in query :
            codePath = "C:\\Users\\singhk3\\Desktop\\Baxter"
            os.startfile(codePath)

        elif 'outlook' in query :
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                toemail = str(input("Enter Email of Whose you want to Send "))
                to = toemail
                speak("What should I say?")
                # content = takeCommand()
                content = input("what would i send")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")