import discord
import os
import requests
import json
from replit import db

from datetime import datetime
from chatterbot import ChatBot
#open discord

client = discord.Client()
chatbot = ChatBot("ModVon Chamg")

amChatBot = False
amThatGuy = False
amModerator = True
"""def calc(inputExp):
    try:
        output = 0
        numbers = []
        opreators = []
        curNum = ""
        for char in inputExp:
            try:
                num = int(char)
                curNum += char

            except:
                if curNum != "":
                    if char == ".":
                        curNum += char
                    
                    else:
                        opreators.append(char)
                        numbers.append(curNum)
                        curNum = ""
                
                else:
                    pass
                    #numbers.append("-" + curNum)
                    #fix neg num prob
        
        numbers.append(str(curNum))
        output += float(numbers[0])

        twoNum = True
        for i in range(0, len(numbers) - 1):
            twoNum = False
            op = opreators[i]
            num = int(numbers[i + 1])
            if op == "+":
                output += num
            
            elif op == "-":
                output -= num
            
            elif op == "*":
                output *= num

            elif op == "/":
                output /= num

            elif op == "^":
                output = output ** num

            else:
                return None

        if twoNum:
            i = 0

            op = opreators[i - 1]
            num = int(numbers[i+1])
            if op == "+":
                output += num
            
            elif op == "-":
                output -= num
            
            elif op == "*":
                output *= num

            elif op == "/":
                output /= num

            elif op == "^":
                output = output ** num

            else:
                return None
            
        return float(output)

    except:
        return None
"""
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("Mod Bot Activated")

@client.event
async def on_connect():
    print("Mod Bot is Awake")
    #await client.get_channel(db["channel"]).send('Mod Bot Is Awake.')
    
@client.event
async def on_disconnect():
    print("Mod bot fell asleep")
    #await client.get_channel(db["channel"]).send('Mod Bot Fell Asleep.')

@client.event
async def on_message(message):
    global chatbot, amChatBot, amThatGuy, amModerator, localGlobalVar
    if message.author != client.user:
        if amChatBot:
            await message.channel.send(chatbot.get_response(str(message.content)))

        if amThatGuy:
            if str(message.content) != "!ThatGuy":
                await message.channel.send(str(message.content))
    roleStr = ""
    for role in message.author.roles:
        roleStr += str(role) + " " 
    f = open("chat.txt", "a")
    f.write("\n" + roleStr + message.author.name + " #" + str(message.author.discriminator) + ": " + str(message.content))
    f.close()
    print(roleStr + message.author.name + " #" + str(message.author.discriminator) + ": " + str(message.content))
    if message.author == client.user:
        pass

    if 'fuck' in str(message.content).lower() or 'shit' in str(message.content).lower():
        await message.delete()
        await message.channel.send('Your message was deleted for abuse of curses')

    if amModerator:

        if message.content.startswith('#news'):
            await message.channel.send('No New News')

        elif message.content.startswith('$help'):
            await message.channel.send('.$projects shows Ivans projects, $time shows the local time, $yes for cool gif, do $no for cool gif, !disconnect disconnects me from the server.')

        elif message.content.startswith('$hello'):
            await message.channel.send('Hello!')
        
        elif message.content.startswith('$bye'):
            await message.channel.send('Bye!')

        elif message.content.startswith('$projects'):
            await message.channel.send('The Circuit Toy: https://replit.com/@IvanChang111/The-Circuit-Toy-Contributors-Lonely-me Conways Game of life: https://replit.com/@IvanChang111/Conways-Game-of-Life-Contributors-Ivan-Sharry#README.md')

        elif message.content.startswith('$time'):
            now = datetime.now()
            currentTime = now.strftime("%d/%m/%Y %H:%M:%S")
            await message.channel.send(str(currentTime))

        elif message.content.startswith('$yes'):
            await message.channel.send('https://tenor.com/view/yes-baby-goal-funny-face-gif-13347383')

        elif message.content.startswith('$no'):
            await message.channel.send('https://tenor.com/view/tonton-tonton-sticker-no-nope-gif-13636081')

        elif message.content.startswith('!help'):
            await message.channel.send('Do !sudo to make me say what you want, !calc for calculator, !run to run python code (DEVS ONLY), !save and !load to save an load varibles (AGAIN DEVS ONLY), do !disconnect to disconnect me from the server.')

        elif message.content.startswith('!sudo'):
            sudoMessage = str(message.content)
            await message.delete()
            await message.channel.send(sudoMessage[6:-1] + sudoMessage[-1])

        elif message.content.startswith('!run'):
            role = discord.utils.get(message.author.roles, name = "Developer")
            if role != None and message.author != client.user:
                inputString = str(str(message.content)[5:-1] + str(message.content)[-1])
                try:
                    exec(inputString)
                    await message.channel.send("Python code successfully executed.")

                except:
                    await message.channel.send("There was a problem when trying to run this code.")
                    print('Oh No! There was a bug!')
            
            else:
                await message.channel.send('You Do Not have Permission to Use This Command ' + str(message.author.name) + ".")

        elif message.content.startswith('!calc'):
            inputString = str(str(message.content)[6:-1] + str(message.content)[-1])
            inputString = inputString.replace("^", "**")
            try:
                answer = eval(inputString.replace(" ", ""))
                if answer != None:
                    await message.channel.send("The answer to that expression should be: " + str(answer))

            except:
                await message.channel.send('I dont understand that command')
        
        elif message.content.startswith('!save'):
            role = discord.utils.get(message.author.roles, name = "Developer")
            if role != None and message.author != client.user:
                inputString = str(str(message.content)[6:-1] + str(message.content)[-1])
                try:
                    db["lgv"] = eval(inputString)
                    await message.channel.send("Python Varible successfully Saved.")

                except:
                    await message.channel.send("There was a problem when trying to save this piece of data")
            
            else:
                await message.channel.send('You Do Not have Permission to Use This Command ' + str(message.author.name) + ".")
        
        elif message.content.startswith('!load'):
            role = discord.utils.get(message.author.roles, name = "Developer")
            if role != None and message.author != client.user:
                inputString = str(str(message.content)[6:-1] + str(message.content)[-1])
                try:
                    await message.channel.send("savedVarible = " + str(db["lgv"]))
                    await message.channel.send("Python Varible successfully Loaded.")

                except:
                    await message.channel.send("There was a problem when trying to load this piece of data.")
            
            else:
                await message.channel.send('You Do Not have Permission to Use This Command ' + str(message.author.name) + ".")

        elif message.content.startswith('!calc'):
            inputString = str(str(message.content)[6:-1] + str(message.content)[-1])
            inputString = inputString.replace("^", "**")
            try:
                answer = eval(inputString.replace(" ", ""))
                if answer != None:
                    await message.channel.send("The answer to that expression should be: " + str(answer))

            except:
                await message.channel.send('I dont understand that command')
    
    if message.content.startswith('!ChatBot'):
        role = discord.utils.get(message.author.roles, name = "Admin")
        if role != None and message.author != client.user:
            if amChatBot:
                amChatBot= False
                await message.channel.send('No Longer a chat bot')

            else:
                amChatBot = True
                await message.channel.send('I am a chat bot Now')

        else:
            await message.channel.send('You Do Not have Permission to Use This Command ' + str(message.author.name) + ".")

    if message.content.startswith('!ThatGuy'):
        role = discord.utils.get(message.author.roles, name = "Admin")
        if role != None and message.author != client.user:
            if amThatGuy:
                amThatGuy = False
                await message.channel.send('No Longer That Guy')

            else:
                amThatGuy = True
                await message.channel.send('I am That Guy Now')

        else:
            await message.channel.send('You Do Not have Permission to Use This Command ' + str(message.author.name) + ".")


    elif message.content.startswith('!Mod'):
        role = discord.utils.get(message.author.roles, name = "Admin")
        if role != None and message.author != client.user:
            if amModerator:
                amModerator = False
                await message.channel.send('No Longer Mod')

            else:
                amModerator = True
                await message.channel.send('I am Mod Now')

        else:
            await message.channel.send('You Do Not have Permission to Use This Command ' + str(message.author.name) + ".")


    elif message.content.startswith('!disconnect'):
        role = discord.utils.get(message.author.roles, name = "Admin")
        if role != None and message.author != client.user:
            await message.delete()
            await message.channel.send('Disconnecting (this will take a few minutes)... ')
            await client.logout()

        else:
            await message.channel.send('You Do Not have Permission to Use This Command ' + str(message.author.name) + ".")

client.run(db["token"])