"""
TODO:  Add semi-realtime prediction
TODO:  Embed youtube links
TODO:  Commands to check if there are games today
        ? Might need database for this
TODO:  Some form of data visualization
TODO:  Host bot adding on a website
TODO:  Optimize code (currently ~38.26 seconds)
        * Time to check game ~9.6 seconds
TODO:  Make bot work for individual users
        ? Store discord ID and selected team?

! Things I've learned:
    * Instead of webscraper, using API (helped with performance and ease of use)
"""


import asyncio
import datetime
import functools
import typing
import time
import discord
from discord.ext import tasks
import nba_data as nba
from scraper import retrieve_youtube_link
from msgcreate import print_game


def to_thread(func: typing.Callable) -> typing.Coroutine:
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        return await asyncio.to_thread(func, *args, **kwargs)

    return wrapper


@to_thread
def sleep_bot():
    curr_time = datetime.datetime.now()
    tomorrow_date = curr_time.date() + datetime.timedelta(days=1)
    tomorrow_datetime = datetime.datetime(
        year=tomorrow_date.year,
        month=tomorrow_date.month,
        day=tomorrow_date.day,
        hour=0,
        minute=0,
        second=0,
    )
    seconds_til_tomorrow = (tomorrow_datetime - curr_time).total_seconds()

    print("Sleeping until tomorrow\n")

    time.sleep(seconds_til_tomorrow)


def discord_bot(secret):
    # If no tzinfo is given then UTC is assumed.
    # times = [
    #     datetime.time(hour=22, minute=30), # 2:30pm
    #     datetime.time(hour=23, minute=30), # 3:30pm
    #     datetime.time(hour=2, minute=30), # 6:30 pm
    #     datetime.time(hour=3, minute=30), # 7:30 pm
    #     datetime.time(hour=5, minute=15), # 9:15 pm
    #     datetime.time(hour=6, minute=0) # 10:30 pm
    # ]

    intents = discord.Intents.default()
    intents.messages = True
    intents.reactions = True
    intents.presences = True
    intents.guilds = True
    intents.members = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"We have logged in as {client.user}")
        await delete_messages.start()

        if not send_message.is_running():
            send_message.start()

    @tasks.loop(seconds=5.0, count=1)
    async def delete_messages():
        user = client.get_user(227261796719919107)
        async for message in user.history():
            if message.author.id == client.user.id:
                await message.delete()
                await asyncio.sleep(0.5)

    @tasks.loop(seconds=1, count=1)
    async def send_message():
        message = ""
        team = "clippers"
        print("In send_message, accessing NBA API")
        game = nba.get_game(team)

        if game is None:
            print("Clippers not playing today")
            await sleep_bot()
            return

        if not nba.is_game_over(game):
            print("Clippers game isn't over yet!")
            return

        message = print_game(game)
        youtube_link = retrieve_youtube_link(team)

        if message:
            user = client.get_user(227261796719919107)
            await user.send(message)
            await user.send(youtube_link)
            await sleep_bot()
            return

    client.run(f"{secret}")
