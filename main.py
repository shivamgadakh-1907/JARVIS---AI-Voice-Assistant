import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import music_library
import requests
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from groq import Groq

groq_client = Groq(
    api_key="Your API key"
)

Eleven_client = ElevenLabs(
    api_key="Your API key"
)

# audio = client.text_to_speech.convert(
#     text="initializing jarvis",
#     voice_id="JBFqnCBsd6RMkjVDRZzb",
#     model_id="eleven_multilingual_v2",
#     output_format="mp3_44100_128",
# )

# play(audio)

recognizer=sr.Recognizer()
# engine=pyttsx3.init()
newsapi="Your API key"


def processcommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://www.whatsapp.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://www.amazon.in")
    elif "open flipkart" in c.lower():
        webbrowser.open("https://www.flipkart.com")
    elif "open chat gpt" in c.lower():
        webbrowser.open("https://www.chatgpt.com")
    elif "open gemini" in c.lower():
        webbrowser.open("https://www.gemini.google.com")
    elif "open x" in c.lower():
        webbrowser.open("https://www.twitter.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        # song=c.lower().replace("play","",1).strip()
        song=c.lower()[5:].strip()
        print("song name:",song)
        if song in music_library.music:
            link=music_library.music[song]
            print("link found:",song)
            webbrowser.open(link)
            print("opening song..")
        else:
            print("song not found")
    elif "news"in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={newsapi}")
        if r.status_code==200:
            #parse the son response
            data=r.json()

            #extract the articales
            articles=data.get('articles',[])

            #print the headlines
            for article in articles:
                speak(article['title'])
        else:
            print("News API error:", r.status_code)

    elif "who am i"in c.lower():
        speak("you are my boss sir and your name is shivam as well as you are the founder of nutron and CEO of next.AI")

    else:
        # let gemini handels the request
        output=aiProcess(c)
        speak(output)


def speak(text):
    # engine.say(text)
    # engine.runAndWait()
    # engine.stop()
    # pyttsx3.speak(text)
    audio = Eleven_client.text_to_speech.convert(
    text=text,
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
    )

    play(audio)


def aiProcess(command):
    completion = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "You are Jarvis, a helpful virtual assistant.Give short, clear answers. Keep responses to 1-3 sentences unless the user asks for detailed information."
            },
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return completion.choices[0].message.content


if __name__=="__main__":
    speak("Initializing jarvis.. ")
    # time.sleep(1)
    # speak("hello boss")

    while True:
        # listen for the wake word "jarvis"
        # obtain audio from the microphone

        r=sr.Recognizer()
       
        # recognizing speech using google
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("listening.....")
                audio=r.listen(source)# jo listen function 2 parameter timeout 2 sec next conversation phrase_time_limitkitnider sunega
            word=r.recognize_google(audio)
            print(word)
            if(word.lower()=="jarvis"):
                speak("Yes boss")
                print("Yes boss")
                #listen for command
                with sr.Microphone() as source:
                    print("jarvis Activeted...")
                    
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    processcommand(command)
                    

        except sr.UnknownValueError:
            print("I could not understand audio")

        except sr.RequestError as e:
            print("audio error;{0}".format(e))

    