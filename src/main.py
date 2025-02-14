"""Navi."""

import openai
from mods import mods
import commands


# [!!] - YOU WILL NEED TO ADD YOUR OWN GPT API KEY HERE!!
openai.api_key = "NO REALLY SYSTEM WILL CRASH IF YOU DONT HAVE A KEY..."
# [!!] - HEY LOOK TWO LINES UP AND READ TO HERE JUST IN CASE...

art = mods.art
breakline = mods.breakline

# Clears the screen and prints out the header
print(art)

# Main loop for gpt / commands
while True:
    # Main input
    chatText = input("Navi> Whats up? \n=> ")

    # Looking out for / commands
    if chatText[0] == '/':
        if chatText == "/stop":
            print("Navi> [!!] - I look forward to seeing you again!")
            exit(0)
        elif chatText in commands.modules.keys():
            print("Navi> [!!] - Runing command:", chatText)
            commands.modules[chatText].run()
        else:
            print(f"Navi> [!!] - Unknown command: '{chatText}'")
            
        print(breakline)

    # Generate AI response if /command not present
    else:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatText,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # Prints out AI response.
        print(response["choices"][0]["text"])
        print(breakline)
