import os
import sys
import xml.etree.cElementTree as ET
from shutil import *

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
----------------------------------------------------------------------------------------------
    """)

def launchPythonConfigFileTwo(name):
    systemosa = os.name

    if systemosa == "nt":
        os.system(f"py {name}.py")
    elif systemosa == "posix":
        os.system(f"python {name}.py")

tree = ET.parse("botconfig.bmfdxml")
root = tree.getroot()

BMFDText()
while (1):
    print("BMFD Menu")
    print("----------------------------------------------------------------------------------------------")

    print("a. Change Bot Settings.")
    print("b. Add commands.")
    print("c. Launch the bot.")

    userType = input("Choose an option > ")

    if userType == "a":
        while (1):
            bottree = ET.parse('botconfig.bmfdxml')
            botroot = bottree.getroot()

            systemosutil = os.name

            if systemosutil == "nt":
                os.system("cls")
            elif systemosutil == "posix":
                os.system("clear")

            BMFDText()

            print("Change bot settings.")
            print("----------------------------------------------------------------------------------------------")

            print("a. Change Token")
            print("b. Change ClientID")
            print("c. Change Prefix")
            print("return. Exit BMFD")

            settingsInput = input("Choose an option > ")

            if settingsInput == "a":
                tokenInput = input("Enter your bot token > ")

                root[0].text = f"{tokenInput}"

                tree.write("botconfig.bmfdxml")

            elif settingsInput == "b":
                clientIdInput = input("Enter the client id of your bot > ")

                root[1].text = f"{clientIdInput}"

                tree.write("botconfig.bmfdxml")
            
            elif settingsInput == "c":
                prefixInput = input("Enter the new prefix > ")

                root[2].text = f"{prefixInput}"

                tree.write("botconfig.bmfdxml")
                    
            elif settingsInput == "return":
                exit()

    elif userType == "b":
        while (1):
            systemosutiltwo = os.name

            if systemosutiltwo == "nt":
                os.system("cls")
            elif systemosutiltwo == "posix":
                os.system("clear")

            BMFDText()

            print("Add Commands.")
            print("----------------------------------------------------------------------------------------------")

            print("a. Basic Command.")
            print("b. Exit")

            addcommandInput = input("Choose an option > ")

            if addcommandInput == "a":
                nameofbasiccmd = input("Name of Basic Command > ")
                messagebasiccmd = input("Message > ")
                botpyfile = open("bot.py", "a")
                botpyfile.write(f"\n    if message.content == PREFIX + '{nameofbasiccmd}': ")
                botpyfile.write(f"\n        await message.channel.send('{messagebasiccmd}') ")
                botpyfile.close()

            elif addcommandInput == "b":
                exit()
    
    elif userType == "c":
        advertInput = input("Do you want to run your bot ? [y,n] > ")

        if advertInput == "y":

            filePy = open("bot.py", "a")
            filePy.write("\n\nclient.run(TOKEN)")
            filePy.close()

            launchPythonConfigFileTwo("bot")    