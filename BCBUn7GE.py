#!/usr/bin/env python3
import discord
import asyncio
import os
import string
import re
import collections
import time
from time import sleep
import datetime
import math
import threading
import random
from random import randint
import requests

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""



onlyChannel = 'bot-topic'



def sendPriv(data):
    data=data[6:]
    r = requests.post("https://kakko.pandorabots.com/pandora/talk?botid=XXXXXX&skin=chat", data={'botcust2': 'YYYYYY','message':data})
    res= find_between( r.text, "<B>Mitsuku:</B> ", "<br> <br> " )
    res = res.replace("<br><br>", "\n")
    res = res.replace("<br>", "\n")

    if res.find("http://www.square-bear.co.uk/mitsuku/gallery") >= 0:
        sv = find_between(res,"http://www.square-bear.co.uk/mitsuku/gallery/",".jpg\"")
        print(sv)
        res = res.replace("<P ALIGN=\"CENTER\"><img src=\"http://www.square-bear.co.uk/mitsuku/gallery/%s.jpg\"></img></P>"%sv,"")
        r2 = requests.get("http://imgur.com/search/score?q=%s&qs=thumbs"%(sv))#relevance/month
        f1 = find_between(r2.text,"<a class=\"image-list-link\"","/>")
        f2 = find_between(f1,"//","\"")
        link = "http://"+f2
        if f2 == "":
            link="http://i.imgur.com/q3OB1hM.jpg"
            print(sv)
 
        em = discord.Embed()#title=sv, color=0xFFFFFF
        #em.set_author(name="CrunchySponge", icon_url=author_avatar_url)
        em.set_image(url=link)
        return (1,res,em)

    if res.find("[IMG]") >= 0:
        sv = find_between(res,"[IMG]http://images.google.co.uk/images?q=","[/IMG]")
        res = res.replace("[IMG]http://images.google.co.uk/images?q=%s[/IMG]"%sv,"")
        r2 = requests.get("http://imgur.com/search/score?q=%s&qs=thumbs"%(sv))#relevance/month
        f1 = find_between(r2.text,"<a class=\"image-list-link\"","/>")
        f2 = find_between(f1,"//","\"")
        link = "http://"+f2
        if f2 == "":
            link="http://i.imgur.com/q3OB1hM.jpg"
            print(sv)
 
        em = discord.Embed()#title=sv, color=0xFFFFFF
        #em.set_author(name="CrunchySponge", icon_url=author_avatar_url)
        em.set_image(url=link)
        return (1,res,em)





    return (0,res,0)

client = discord.Client()
client.login('email', 'password')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')




@client.event
async def on_message(message):

    isDM = "Direct Message with" in str(message.channel)
    if onlyChannel != "" and str(message.channel) != onlyChannel and isDM == False:
        return



    if message.content.startswith('!chat'):
        data=sendPriv(message.content)
        if data[0] == 1:
            await client.send_message(message.channel, data[1],embed=data[2])
        else:
            await client.send_message(message.channel, data[1])




client.run('DISCORD BOT TOKEN')