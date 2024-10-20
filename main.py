#Modules
from bs4 import BeautifulSoup
from colorama.ansi import clear_screen
from pyfiglet import SHARED_DIRECTORY, Figlet  #These two are for colored text
from colorama import init, Fore  # ^
import subprocess
import sys
from colorama import init
import os

# Initialize colorama
init(strip=not sys.stdout.isatty())

# Create Figlet object
f = Figlet(font='standard')

# Define the ASCII art as a string
ascii_art = """
  ________ .__                      __          
 /  _____/ |  |__    ____   _______/  |_        
/   \  ___ |  |  \  /  _ \ /  ___/\   __\       
\    \_\  \|   Y  \(  <_> )\___ \  |  |         
 \______  /|___|  / \____//____  > |__|         
        \/      \/             \/               

  _________                __                   
 /   _____/  ____   ____  |  | __  ____ _______ 
 \_____  \ _/ __ \_/ __ \ |  |/ /_/ __ \_  __ \\
 /        \\\  ___/\\  ___/ |    < \  ___/ |  | \/
/_______  / \\___  >\\___  >|__|_ \\ \___  >|__|   
        \/      \/     \/      \/     \/        
"""

# Print colored ASCII art
print(Fore.BLUE + ascii_art)

print(Fore.RED)
#Welcome/Startup screen
print("  An Open Source Intelligence Gathering Framework")
print("       Created by: MRX & KRYPTON")
print("       Team: FR13NDS")
print("               Version: " + Fore.LIGHTCYAN_EX + "1.0")
print("          " + Fore.WHITE + "Platform:" + Fore.BLUE + "Linux")
print(Fore.WHITE)

#Menu screen
print("       " + Fore.RED + "[??] Choose an option:")
print("       " + Fore.RED + "[" + Fore.BLUE + "1" + Fore.RED + "]" +
      Fore.WHITE + "  Domain Information")
print("       " + Fore.RED + "[" + Fore.BLUE + "2" + Fore.RED + "]" +
      Fore.WHITE + "  Social Media Information")
print("       " + Fore.RED + "[" + Fore.BLUE + "3" + Fore.RED + "]" +
      Fore.WHITE + "  IP Address Information")
print("       " + Fore.RED + "[" + Fore.BLUE + "4" + Fore.RED + "]" +
      Fore.WHITE + "  Email Address Information")
print("       " + Fore.RED + "[" + Fore.BLUE + "5" + Fore.RED + "]" +
      Fore.WHITE + "  Person Information")
print("       " + Fore.RED + "[" + Fore.BLUE + "6" + Fore.RED + "]" +
      Fore.WHITE + "  Extract Metadata packets from image")
print("       " + Fore.RED + "[" + Fore.BLUE + "7" + Fore.RED + "]" +
      Fore.WHITE + "  Update Ghost Framework")
print("       " + Fore.RED + "[" + Fore.BLUE + "8" + Fore.RED + "]" +
      Fore.WHITE + "  About")
print("       " + Fore.RED + "[" + Fore.BLUE + "9" + Fore.RED + "]" +
      Fore.WHITE + "  Exit")
print("\n")
choice = input("Enter your choice: ")

#Choice config
choice1 = "1"
choice2 = "2"
choice3 = "3"
choice4 = "4"
choice5 = "5"
choice6 = "6"
choice7 = "7"
choice8 = "8"
choice9 = "9"

#Tools exe
# Domain Information
if choice == choice1:
      print(Fore.YELLOW + "Domain Information\n" + Fore.WHITE)
      domain = input("Enter the domain name: ")
      print(Fore.CYAN + "Running domain information tools...\n" + Fore.WHITE)
      subprocess.run(f"sh /root/Documents/Ghost/main.sh {domain} 1", shell=True)

      # Nmap
      print(Fore.CYAN + "Running Nmap...\n" + Fore.WHITE)
      subprocess.run(f"sh /root/Documents/Ghost/nmap.sh {domain}", shell=True)

# Social Media Information
if choice == choice2:
      print(Fore.YELLOW + "Social Media Information\n" + Fore.WHITE)
      user = input("Enter the user: ")
      print(Fore.CYAN + "Hunting down social media accounts...\n" + Fore.WHITE)
      subprocess.run(f"sh /root/Documents/Ghost/person_info.sh {user}", shell=True)

# IP Address Information
if choice == choice3:
      print(Fore.YELLOW + "IP Address Information\n" + Fore.WHITE)
      ip = input("Enter the IP address: ")
      print(Fore.CYAN + "Gathering information...\n" + Fore.WHITE)

      #IP info
      subprocess.run(f"sh /root/Documents/Ghost/ip_lookup.sh {ip}", shell=True)

# Email Address Information
if choice == choice4:
      print(Fore.YELLOW + "Email Address Information\n" + Fore.WHITE)
      email = input("Enter the Email address: ")
      print(Fore.CYAN + "Gathering information...\n" + Fore.WHITE)

      #IP info
      subprocess.run(f"sh /root/Documents/Ghost/email_info.sh {email}", shell=True)

#Exit
#about
if choice == choice8:
      print(
          Fore.CYAN +
          "Ghost Framework is an Open Source Intelligence (OSINT) gathering framework, which aids in the collection of information about targets, such as individuals, businesses, and organizations. It utilizes a variety of tools and techniques to gather data from public sources, such as social media, websites, and public records."
      )
      print(
          "The information gathered by Ghost Framework can be used for a variety of purposes, including: "
      )
      print("• Investigative journalism")
      print("• Security research")
      print("• Business intelligence")
      print("• Threat intelligence")
      print("• Law enforcement")
      print("• Personal investigation")
      print(
          "Ghost Framework is designed to be user-friendly and versatile, allowing users to customize their searches to meet their specific needs."
      )
      print(
          "It is a powerful tool that can be used to gather a wealth of information about any target."
      )
      print(
          "Ghost Framework is developed and maintained by MRX & KRYPTON, and is a part of the FR13NDS team. It is an open-source project, and contributions are always welcome."
      )
      print(
          "The framework is constantly being updated with new features and tools, and the developers strive to provide the most comprehensive and user-friendly OSINT platform available."
      )
      print(
          "In addition to the tools and features mentioned above, Ghost Framework also includes a number of other useful features, such as:"
      )
      print(
          "• A command-line interface (CLI) for easy navigation and interaction"
      )
      print("• A graphical user interface (GUI) for a more visual experience")
      print("• Support for multiple operating systems")
      print("• A comprehensive documentation library")
      print("• A large community of users and developers")
      print(
          "Ghost Framework is a powerful and versatile tool that can be used to gather a wealth of information about any target. It is a valuable resource for anyone who needs to conduct OSINT investigations."
      )
      print("Ghost Framework is also available on Github")

###
