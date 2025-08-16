import time
import sys
import random

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
PINK = "\033[95m"
RESET = "\033[0m"

# Function to simulate typing effect
def slow_print(text, delay=0.05, color=RESET):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Function to simulate loading/progress bar
def progress_bar(task_name):
    slow_print(f"{task_name}...", 0.05, RED)   # progress messages in RED
    for i in range(0, 101, random.randint(5, 15)):
        if i > 100:
            i = 100
        sys.stdout.write(f"\r{RED}[{i*'█' + (100-i)*' '}] {i}%{RESET}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.2, 0.5))
    print("\n")

# ASCII Banner (Pink)
banner = PINK + r"""

 ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗   
 ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝              
 ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗             
 ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║             
 ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                       
 ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗  
 ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝              
    ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝                
    ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗               
    ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗              
    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ 
    Tool created by -Anonymous-Teach | Hacking Termux
""" + RESET

print(banner)

# Options
slow_print("Select an option to process:\n")
slow_print("1. Post")
slow_print("2. Story")
slow_print("3. ID")
slow_print("4. Reel\n")

option = input("Enter option number: ")

# Input depending on option
if option == "3":
    username = input("Enter the Instagram username: ")
    slow_print(f"\nVerifying Instagram account: {username} ...\n", 0.05, RED)
    progress_bar("Checking account status")
else:
    url = input("Enter the Instagram URL: ")
    slow_print(f"\nVerifying Instagram content: {url} ...\n", 0.05, RED)
    progress_bar("Checking content status")

# Simulate network check and additional processing
slow_print("Connecting to Instagram servers...", 0.05, RED)
progress_bar("Establishing secure connection")
slow_print("Analyzing data packets...", 0.05, RED)
progress_bar("Processing information")
slow_print("Finalizing request...", 0.05, RED)
progress_bar("Completing action")

# Random fake outcome messages (Green)
fake_messages = [
    "Action completed successfully!",
    "Verification successful!",
    "Content/account processed!",
    "No issues detected, operation complete!"
]

slow_print(f"\n✅ {random.choice(fake_messages)}", 0.05, GREEN)
