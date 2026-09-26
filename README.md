# PyBot 🤖

A simple rule-based chatbot built in Python. PyBot responds to greetings, tells jokes, gives career advice, shares the date/time, and more — all through basic keyword matching.

## Features

- Friendly greetings and small talk
- Random jokes on demand
- Career advice for aspiring programmers
- Current date and time lookup
- Fun facts about Python
- Simple `help` menu to list all commands
- Graceful exit with `bye`

## Requirements

- Python 3.x (no external libraries needed — uses only the built-in `random` and `datetime` modules)

## How to Run

1. Save the script as `pybot.py`.
2. Open a terminal in the same folder.
3. Run:

   ```bash
   python pybot.py
   ```

4. Start chatting! Type `help` to see available commands.

## Example Commands

| Command                  | What it does                          |
|---------------------------|----------------------------------------|
| `hello` / `hi` / `hey`    | Get a greeting                         |
| `how are you`             | Ask PyBot how it's doing               |
| `name`                    | Ask PyBot its name                     |
| `joke`                    | Hear a random programming joke         |
| `age`                     | Ask how old PyBot is                   |
| `date`                    | Get today's date                       |
| `time`                    | Get the current time                   |
| `career advice`           | Get a random piece of career advice    |
| `bored`                   | Get a suggestion for something to do   |
| `python`                  | Learn a fact about Python              |
| `help`                    | See the full list of commands          |
| `bye` / `exit` / `quit`   | End the conversation                   |

## Example Session

```
======================================
          WELCOME TO PYBOT
======================================
Hello! I am PyBot.
Type 'help' to see what I can do.
Type 'bye' to exit.

You: hello
PyBot: Hi!
You: joke
PyBot: Why do programmers prefer dark mode? Because light attracts bugs!
You: bye
PyBot: Goodbye!
Thanks for chatting with me!
```

## Possible Improvements

- Add natural language processing for more flexible input matching
- Store conversation history to a log file
- Add more categories of responses (weather, trivia, etc.)
- Convert to a GUI or web app using Tkinter or Flask

## License

Free to use and modify for personal or educational purposes.
