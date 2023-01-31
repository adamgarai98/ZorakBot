import logging
import os
import sys

import discord
from discord.ext import commands
from utilities.core.args_utils import parse_args
from utilities.core.logging_utils import setup_logger
from utilities.core.mongo import initialise_bot_db

logger = logging.getLogger("discord")
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
bot.remove_command("python")


def load_cogs(bot):
    for f in os.listdir("zorak_bot/cogs"):
        if f.endswith(".py"):
            if not f.startswith("_"):
                bot.load_extension("cogs." + f[:-3])
    return bot


def run_bot(bot, discord_token):
    if discord_token:
        bot.run(discord_token)
    else:
        if len(sys.argv) > 1:
            TOKEN = sys.argv[1]
            bot.run(TOKEN)
        else:
            raise Exception("ERROR: You must include a bot token.")


if __name__ == "__main__":
    args = parse_args()
    setup_logger(level=args.log_level, stream_logs=args.console_log)
    run_bot(
        load_cogs(initialise_bot_db(bot)), args.discord_token
    )  # If args.discord_token is None, it will use the TOKEN env variable.