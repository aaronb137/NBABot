from clipperbot import discord_bot
from gcpsecret import retrieve_secret

if __name__ == "__main__":
    # time_start = time.time()
    secret = retrieve_secret()
    discord_bot(secret)
    # time_end = time.time()
    # print(time_end-time_start)
