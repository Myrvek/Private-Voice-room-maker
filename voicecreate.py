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


@bot.command()
async def help( ctx  ):
	embed=discord.Embed(title="**Все команды бота**", color=0x56d625)
	embed.set_author(name="Твой жорик")
	embed.add_field(name="Общие команды  \n `() Не обезательный аргумент` \n `[] Обезательный аргумент`", value="b_thx Сказать спасибо или дать репу \n b_my_thx Моя репа или спасибо \n b_avatar(пинг)Покозать аву себя или пользователя \n b_servercount показывает где я есть \n b_ping посмотреть свой пинг \n b_ran_avatar случайная аниме ава \n b_hello привет боту \n b_profile(пинг) твой профиль или другого", inline=False)
	embed.add_field(name="Веселости  \n `() Не обезательный аргумент` \n `[] Обезательный аргумент`", value="b_pat [пинг] погладить \n b_slap [пинг] ударить\n b_kiss [пинг] поцеловать\n b_hug[пинг]обнять\n b_wiki[Текст]Википедия\n b_knb сыграть в КНБ! \n b_man Stonks \n b_wea [Город] Погода в городе \n b_numbers сыграть в угодайку n b_calc [число] [Оператор] [число] калькулятор\n b_remind [Время] [Текст] Напомнить \n  b_serverinfo Инфо о сервере ", inline=True)
	embed.add_field(name="Модераторское \n `() Не обезательный аргумент` \n `[] Обезательный аргумент`", value="b_kick[пинг][причина]кик человека\n b_ban[пинг](причина](время]бан человека\n b_unban[айди]разбан\n  \n b_clear[Кол-во сообшений] \n b_mute [человек] [прчина]вечный мут", inline=True)
	embed.add_field(name="Другое \n `() Не обезательный аргумент` \n `[] Обезательный аргумент`", value="b_ball[Вопрос] Кинуть шар \n b_dice[1 число] [2 число] сыграть в кости \n b_giveaway[Время в секундна][Вещь] Конкурс b_gl [Запрос] Я гуглю за вас( \n b_c0t Котики!!  \n b_vote Проголосовать за меня", inline=True)
	embed.add_field(name="Предложка \n `() Не обезательный аргумент` \n `[] Обезательный аргумент`", value="b_suggest [Идея]  предложить идею \n b_suggest_set  [канал] поставить канал идей \n b_suggest_off отключить", inline=True)
	embed.add_field(name="Жалобы \n `() Не обезательный аргумент` \n `[] Обезательный аргумент`", value="b_report [Жалобы]  жалобы на сервере или юзера \n b_report_set  [канал] поставить канал жалоб \n b_report_off  отключить", inline=True)
	embed.add_field(name="Спецальное \n `() Не обезательный аргумент` \n `[] Обезательный аргумент`", value="b_flag Сыграть в игру угодай флаг \n b_marry [Пинг] Поженится \n b_divorce Развестисть \n b_sap Сыграть в сапера", inline=True)
	embed.add_field(name="Приватные войсы \n `() Не обезательный аргумент` \n `[] Обезательный аргумент`", value="Для этого была создана отдельная мега красивая команлда b_privhelp", inline=True)
	await ctx.send( embed = embed )

@bot.event
async def on_ready():
    print('Logged in ')


bot.run('NzI2NzQyNzg0ODk1MzUyODcy.XwIBiA.NGdCMlVzujhywHPMjCfdVDvkmCg')
