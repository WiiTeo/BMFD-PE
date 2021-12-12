import os
import sys
import pip
import lib.bmfdPip as bmfdpip
import lib.bmfdos as bmfdos
import xml.etree.cElementTree as ET
from shutil import *

# BMFD Python
# By WiiTeo

if os.path.isdir("bot"):
    pass
else:
    os.mkdir("bot")
    os.chdir("bot")
    configFile = open("botlist.txt", "w")
    configFile.write("# BMFD BotList")
    configFile.close()

# This part is just for fun.

def BMFDText():
    print("""

BBBBBBBBBBBBBBBBB   MMMMMMMM               MMMMMMMMFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDDDD        
B::::::::::::::::B  M:::::::M             M:::::::MF::::::::::::::::::::FD::::::::::::DDD     
B::::::BBBBBB:::::B M::::::::M           M::::::::MF::::::::::::::::::::FD:::::::::::::::DD   
BB:::::B     B:::::BM:::::::::M         M:::::::::MFF::::::FFFFFFFFF::::FDDD:::::DDDDD:::::D  
B::::B     B:::::B  M::::::::::M       M::::::::::M F:::::F      FFFFFF  D:::::D      D:::::D 
B::::B     B:::::B  M:::::::::::M     M:::::::::::M  F:::::F               D:::::D     D:::::D
B::::BBBBBB:::::B   M:::::::M::::M   M::::M:::::::M  F::::::FFFFFFFFFF     D:::::D     D:::::D
B:::::::::::::BB    M::::::M M::::M M::::M M::::::M  F:::::::::::::::F     D:::::D     D:::::D
B::::BBBBBB:::::B   M::::::M  M::::M::::M  M::::::M  F:::::::::::::::F     D:::::D     D:::::D
B::::B     B:::::B  M::::::M   M:::::::M   M::::::M  F::::::FFFFFFFFFF     D:::::D     D:::::D
B::::B     B:::::B  M::::::M    M:::::M    M::::::M  F:::::F               D:::::D     D:::::D
B::::B     B:::::B  M::::::M     MMMMM     M::::::M  F:::::F               D:::::D    D:::::D 
BB:::::BBBBBB::::::BM::::::M               M::::::MFF:::::::FF           DDD:::::DDDDD:::::D  
B:::::::::::::::::B M::::::M               M::::::MF::::::::FF           D:::::::::::::::DD   
B::::::::::::::::B  M::::::M               M::::::MF::::::::FF           D::::::::::::DDD     
BBBBBBBBBBBBBBBBB   MMMMMMMM               MMMMMMMMFFFFFFFFFFF           DDDDDDDDDDDDD      
----------------------------------------------------------------------------------------------
                                 Python Edition - By WiiTeo
---------------------------------------------------------------------------------------------
    """)

BMFDText()

choix = input("Do you have Discord.py installed ? [y,n] > ")

if choix == "y":
    pass

elif choix == "n":
    installDiscordPy = input("Do you want to install discord.py ? [y,n] > ")

    if installDiscordPy == "y":
        bmfdpip.install("discord.py")
        bmfdpip.install("discord")

        bmfdos.osclear()
        print("Please restart BMFD to complete discord.py installation.")
        exit()
    elif installDiscordPy == "n":
        print("Sorry, but BMFD require Discord.py to work. Exit with code 1")
        exit()

bmfdos.osclear()

cwdcurrenst = os.getcwd()

BMFDText()

choixBot = input("Do you have any bot on BMFD ? [y,n] > ")

if choixBot == "y":
    inputChoixBot = input("Name of the bot ? > ")

    os.chdir("bot")

    if os.path.isdir(inputChoixBot):
        os.chdir(inputChoixBot)
        bmfdos.launchPythonConfigFile(f"cf_{inputChoixBot}")
        exit()

    else:
        print(f"Sorry, but the bot {inputChoixBot} does not exist. Exit with code 2.")
        exit()
    
elif choixBot == "n":
    askPersonIfCreateBot = input("Do you want to create a bot ? [y,n] > ")

    if askPersonIfCreateBot == "y":
        os.chdir("bot")
        askPersonNameForCreateBot = input("Name of your bot ? > ")

        botlistWriteName = open("botlist.txt", "a")
        botlistWriteName.write(f"\nBot Name : {askPersonNameForCreateBot}")
        botlistWriteName.close()

        if askPersonNameForCreateBot == "":
            print("Sorry, if you don't enter bot name, we can't create bot. Exit with code 3.")

        else:
            os.mkdir(askPersonNameForCreateBot)
            os.chdir(askPersonNameForCreateBot)

            botReadmeCreateFile = open("README.md", "a")
            botReadmeCreateFile.write(f"# {askPersonNameForCreateBot} Bot")
            botReadmeCreateFile.write("\nBot created with BMFD Python Edition.")
            botReadmeCreateFile.write("\nThis bot use discord.py api.")
            botReadmeCreateFile.close()

            root = ET.Element("BMFD")
            token = ET.SubElement(root, "Token")
            clientId = ET.SubElement(root, "ClientID")
            prefix = ET.SubElement(root, "Prefix")

            tree = ET.ElementTree(root)
            tree.write("botconfig.bmfdxml")
            
            botPythonCreateBotPy = open("bot.py", "a")
            botPythonCreateBotPy.write("# Generate with BMFD Python Edition")
            botPythonCreateBotPy.write("""\nimport os
import discord
import xml.etree.ElementTree as ET

tree = ET.parse('botconfig.bmfdxml')
root = tree.getroot()

TOKEN = root[0].text
PREFIX = root[2].text

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is connected to Discord !')

async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}bmfd':
        await message.channel.send('BMFD Python Edition. By WiiTeo. https://github.com/WiiTeo/BMFD/')
""")
            botPythonCreateBotPy.close()

            osusing = os.name
            cwdcurrent = os.getcwd()

            print(cwdcurrent)

            if osusing == "nt":
                copy("../../bmfd_files/cf_bot/__init__.py", cwdcurrent)
                os.rename("__init__.py", f"cf_{askPersonNameForCreateBot}.py")
                bmfdos.launchPythonConfigFile(f"cf_{askPersonNameForCreateBot}")