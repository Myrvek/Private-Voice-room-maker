# -*- coding: utf8 -*-

import discord
import math
import asyncio
import aiohttp
import json
from discord.ext import commands
from random import randint
import traceback
import sqlite3
import sys
import os

bot = commands.Bot(command_prefix=".")
bot.remove_command("help")



@bot.event
async def on_ready():
    print('Logged in ')


bot.run('Сюда токен')
