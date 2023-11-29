import datetime
import random
import requests
from pydictionary import PyDictionary
import pyjokes
from googlesearch import search

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_weather(city):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        temperature = data['main']['temp']
        return f"The current temperature in {city} is {temperature} Kelvin."
    except Exception as e:
        return f"Failed to get weather information. {str(e)}"

def get_joke():
    return pyjokes.get_joke()

def remind_user():
    reminder = input("What would you like to be reminded of? ")
    print(f"I'll remind you of '{reminder}' later.")

def search_google(query):
    results = list(search(query, num=3, stop=3))
    print("Top 3 search results:")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result}")

def define_word(word):
    dictionary = PyDictionary()
    definition = dictionary.meaning(word)
    return f"The definition of '{word}' is: {str(definition)}" if definition else f"Couldn't find the definition of '{word}'."

def ai_assistant():
    print("Hello! I am your AI assistant. How can I assist you today?")
    user_input = input("Type your question or command: ").lower()

    if "hello" in user_input:
        print("Hello there! How can I help you?")
    elif "how are you" in user_input:
        print("I'm just a program, but thanks for asking!")
    elif "bye" in user_input:
        print("Goodbye! If you need anything, feel free to ask.")
    elif "your name" in user_input:
        print("I'm your AI assistant.")
    elif "calculate" in user_input:
        try:
            result = eval(user_input.split("calculate")[1])
            print("Result:", result)
        except:
            print("Invalid calculation. Please check your input.")
    elif "date" in user_input:
        print("Current date is:", get_current_date())
    elif "time" in user_input:
        print("Current time is:", get_current_time())
    elif "weather" in user_input:
        city = input("For which city would you like to get the weather? ")
        print(get_weather(city))
    elif "joke" in user_input:
        print(get_joke())
    elif "reminder" in user_input:
        remind_user()
    elif "search" in user_input:
        query = input("What do you want to search on Google? ")
        search_google(query)
    elif "help" in user_input:
        print("I can assist you with various tasks such as calculations, date and time, jokes, weather, word definitions, and more.")
    elif "define" in user_input:
        word = input("What word would you like to define? ")
        print(define_word(word))
    else:
        print("I'm sorry, I don't understand that command. Can you please rephrase or ask something else?")

# Run the AI assistant
ai_assistant()
