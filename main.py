import speech_recognition as sr
import os
import pyttsx3
import requests
import wiki
import YT_play
from news import *
import randfacts
import openai


chat_st = ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = api_key
    chatStr += f"Subhash: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def smart(prompt):
    openai.api_key = api_key
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)
        text = r.recognize_google(audio)
        a=1
        print(f"Subhash: {text}")
    return text

def say(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    engine = pyttsx3.init()
    engine.setProperty('rate', 235)
    print('Welcome to Jarvis A.I sir')
    say("Welcome to Jarvis AI sir")
    while True:
        query = take_command()
        if 'wikipedia'.lower() in query.lower():
            say("What do you want to learn about sir")
            print("What do you want to learn about sir")
            text = take_command()
            say(f'searching {text} in wikipedia')
            info = wiki.Info()
            info.get_info(text)

        elif ('youtube'.lower() in query.lower()) or ('play'.lower() in query.lower()):
            say("What would you like to watch sir")
            print("What would you like to watch sir")
            video = take_command()
            fun = YT_play.entertainment()
            fun.play(video)

        elif ('news'.lower() in query.lower()) or ('latest'.lower() in query.lower()):
            print("Getting the latest updates sir")
            say("Getting the latest updates sir")
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                say(arr[i])

        elif('fact'.lower() in query.lower()):
            say("sure sir")
            fact = randfacts.get_fact()
            print(fact)
            say("Did you that" + fact)

        elif ('quit'.lower() in query.lower()) or ('end'.lower() in query.lower()) or ('shut'.lower() in query.lower()):
            say("Shutting down sir...")
            print("Shutting down sir...")
            break

        elif "Using openai".lower() in query.lower():
            smart(prompt=query)

        else:
            print("Chatting...")
            chat(query)

