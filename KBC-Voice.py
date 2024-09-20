import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        # speak("Good Morning Sir!")
        speak("Namaste Sir. Jai Shree Ram")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

    # speak("I am Personal Assistant Sir. Please tell me how may I help you") 
    speak("Welcome to the KBC. Kon baneaga crorepati") 
    speak("Here is the first question. Who is the present prime minister of india. option a. Narendra das Modi,b. Amit Shah, c. Aditya yoginath, d. jay-Shankar") 
    
def option():
    if(ch=='modi' or ch=='Narendra das Modi' or ch=='a' or ch=='1'):
        speak("congrulation sir. it is Correct answer..You Won Rs 1000")
    else:
        speak("Sorry sir. This is a wrong answer, Try again or Better luck next time..👍")
wishMe()
ch=str(input("Enter the Option(1-4)/(A-D)/(a-d) :- "))
option()

if (ch=='1' or ch=='a' or ch=='modi' or ch=='Narendra das Modi'):
    speak("Next Question Number-2 is Who invented C programming language? . option a. Charles Babbage, b. Dennis Ritchie, c. Bill Gates, d. Lady Lovelace Ada")
    ch=str(input("Enter the option :- "))
    
    if(ch=='Dennis Ritchie' or ch=='2' or ch=='b' or ch=='B'):
        speak("congrulation sir. it is Correct answer..😎 and You won the Rs 2000")
    else:
        speak("Sorry sir. This is a wrong answer, Try again or Better luck next time..😒")


if (ch=='Dennis Ritchie' or ch=='2' or ch=='b' or ch=='B'):

    speak("Next Question is What is the correct value to return to the operating system upon the successful completion of a program?. option a. Program don't return any value,b. 1, c. Error, d. 0")

    ch=str(input("Enter the option :- "))
    if(ch=='0' or ch=='4' or ch=='d' or ch=='D'):
        speak("congrulation sir. it is Correct answer..and You won the Rs 3000")
    else:
        speak("Sorry sir. This is a wrong answer, Try again or Better luck next time..👍")

else:
    speak("You give wrong answer that's why you are out from the game...")


