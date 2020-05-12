"""
voice assistant 

"""
import pyttsx3                                 # Module used for voice
import datetime                                # for time purpose
import speech_recognition as sr                # Speech recoganition module
import wikipedia                               # for searching wikipedia
import webbrowser                              # for opening website in default browser 
import os                                      # for playing music and other computer related operations
import smtplib                                 # for sending email 

engine = pyttsx3.init('sapi5')                     # Sapi5 is windows inbuilt voice which is used    
voices = engine.getProperty('voices')              # getting the properties 
engine.setProperty('voice',voices[0].id)           # setting the voice 0 for male and 1 for female


"""
the below function takes care 
of the speech which has to be 
spoken by the assistant
"""
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# function to greet
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=00 and hour < 12:
        speak("Good morning sir")
    
    elif hour >=12 and hour < 16 : 
        speak("Good afternoon sir")
    
    elif hour >= 16 and hour < 24:
        speak("good evening sir")

    speak("I am Jarvis , How may i help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
    
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language= "en-in")
        print(f"user : {query}\n")

    except Exception as e:
        #print(e)
        print("couldn't understand please repat again")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login("<your email id>","<your password>")
    server.sendmail("<your email id>",to,content)
    server.close()
wishMe()
while True:
    
    query = takeCommand().lower()
    
    if 'wikipedia' in query:
        speak("searching wikipedia")
        query = query.replace('wikipedia',"")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open google' in query:
        webbrowser.open("google.com")
    
    elif 'open youtube.com' in query:
        webbrowser.open("youtube.com")

    elif 'play music' in query:
        musicdir= "H:\\S O N G S"
        songs = os.listdir(musicdir)
        print(songs)
        os.startfile(os.path.join(musicdir,songs[0]))
    
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")    

    elif 'open github' in query:
        webbrowser.open("github.com")   

    elif 'the time' in query:

        time = datetime.datetime.now().strftime("%H:%M:%S")
        time= time.split(':')



        #strtime = datetime.datetime.now().strftime()
        speak(f"Sir, the time is{time[0]}hours,{time[1]}minutes, {time[2]} seconds")
        #print(strtime)
          


    elif 'open code' in query:
        codeloc = 'C:\\Users\\Nagendrra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
        os.startfile(codeloc)
 
    elif 'exit' in query:
        break

    elif 'email to prasad' in query:
        
        try:
            speak("what should i send , sir")
            content = takeCommand()
            to = '<destination email id>'
            sendEmail(to,content)
            speak("your email has been sent, sir")

        except Exception as e :
            print(e)
            speak("sorry the email was not sent ")








