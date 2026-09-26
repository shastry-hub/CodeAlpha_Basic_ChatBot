import random
from datetime import datetime

def tell_joke():
    jokes = [
        "Why did the computer go to the doctor? Because it had a virus!",
        "Why was the computer cold? Because it left its Windows open!",
        "Why do programmers prefer dark mode? Because light attracts bugs!"
    ]
    return random.choice(jokes)


def career_advice():
    advice = [
        "Keep learning Python and practice small projects.",
        "Learn Python, Java, SQL and Data Structures.",
        "Build projects and upload them to GitHub.",
        "Practice coding regularly."
    ]
    return random.choice(advice)


def chatbot():

    print("======================================")
    print("          WELCOME TO PYBOT")
    print("======================================")
    print("Hello! I am PyBot.")
    print("Type 'help' to see what I can do.")
    print("Type 'bye' to exit.")
    print()

    while True:

        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey", "hii"]:
            responses = [
                "Hi!",
                "Hello! How can I help you?",
                "Hey! Nice to meet you!"
            ]
            print("PyBot:", random.choice(responses))

        elif user_input in ["how are you", "how are you?"]:
            print("PyBot: I'm fine, thanks!")

        elif user_input in ["fine", "good", "i am fine"]:
            print("PyBot: That's great to hear!")

        elif user_input in ["name", "what is your name"]:
            print("PyBot: My name is PyBot.")

        elif user_input in ["joke", "tell me a joke"]:
            print("PyBot:", tell_joke())

        elif user_input in ["age", "how old are you"]:
            print("PyBot: I don't have a real age. I am a Python chatbot!")

        elif user_input in ["date", "what is the date"]:
            today = datetime.now()
            print("PyBot: Today's date is",
                  today.strftime("%d-%m-%Y"))

        elif user_input in ["time", "what is the time"]:
            current_time = datetime.now()
            print("PyBot: The current time is",
                  current_time.strftime("%I:%M %p"))

        elif user_input in ["career", "career advice"]:
            print("PyBot:", career_advice())

        elif user_input in ["bored", "i am bored"]:
            print("PyBot: Try learning something new or coding a small project!")

        elif user_input in ["python", "tell me about python"]:
            print("PyBot: Python is a popular programming language.")
            print("It is used for web development, automation, AI and data science.")

        elif user_input == "help":
            print()
            print("You can ask me:")
            print("hello")
            print("how are you")
            print("name")
            print("joke")
            print("age")
            print("date")
            print("time")
            print("career advice")
            print("bored")
            print("python")
            print("bye")

        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print("PyBot: Goodbye!")
            print("Thanks for chatting with me!")
            break

        else:
            print("PyBot: Sorry, I don't understand that.")
            print("Type 'help' to see what I can do.")


chatbot()
