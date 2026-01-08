import random
import time
import json
import os
import sys

# --- Color Constants ---
G = "\033[92m" # Green
B = "\033[94m" # Blue
Y = "\033[93m" # Yellow
R = "\033[91m" # Red
W = "\033[0m"  # White/Reset

def slow_type(text):
    """Adds a realistic typing effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def load_responses():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("\033[92mBot: I am under process... updating my brain. Please restart me later.\033[0m")
        time.sleep(2)
        sys.exit()

def chat_bot():
    bot_data = load_responses()
    
    
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{Y}{B}=== NEON-BOT SYSTEM ONLINE ==={W}")
    time.sleep(1)
    print(f"{G}----[STATUS: ACTIVE]----{W}")
    print(f"{B}--[Commands: HI, HOW ARE YOU, JOKE, QUIT]--{W}\n")

    user_name = ""
    while not user_name:
        print(f"{G}Bot:{W} Identity unknown. Please enter your name.")
        user_name = input(f"{B}Me (Name): {W}").strip()
        if not user_name:
            print(f"{Y}Warning: Input cannot be empty.{W}")

    slow_type(f"{G}Bot:{W} Access granted. Hello {user_name}. How can I assist you?")

    while True:
        user = input(f"\n{B}{user_name}: {W}").lower().strip()

        if "quit" or  "exit"or "bye" in user:
            slow_type(f"{G}Bot:{W} Powering down... TATA Goodbye {user_name}.")
            break
        
        elif user in ["hi", "hello", "hey"]:
            msg = random.choice(bot_data["greetings"])
            print(f"{G}Bot:{W} ", end="")
            slow_type(msg)

        elif user in ["how are you", "whats up", "how is it going", "how are you?"]:
            msg = random.choice(bot_data["how_are_you"])
            print(f"{G}Bot:{W} ", end="")
            slow_type(msg)

        elif "random" in user or "fact" in user or "tell me" in user:
            msg = random.choice(bot_data['random_facts'])
            print(f"{G}Bot:{W} ", end="")
            slow_type(msg)
        
        elif "funny" in user or "joke" in user:
            msg = random.choice(bot_data['funny'])
            print(f"{G}Bot:{W} ", end="")
            slow_type(msg)
            
        else:
            msg = random.choice(bot_data['fallback'])
            print(f"{G}Bot:{W} ", end="")
            slow_type(msg)

if __name__ == "__main__":
    chat_bot()

    ''' run this on terminal '''