"""
Pinning command.
"""
import logging
import discord
from datetime import datetime
from discord.ext import commands

logger = logging.getLogger(__name__)


class GeneralPin(commands.Cog):
    """
    # Echos and pins a message
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def pin(self, ctx, message_link: discord.Message):
        """
        Echos and pins a message
        """
        logger.info("%s used the %s command."
                    , ctx.author.name
                    , ctx.command)
        
        general_channel = await self.bot.fetch_channel(self.bot.server_settings.normal_channel["general_channel"])
        embed = embed_pin(message_link)
        #await general_channel.send(message_link.content)

        await general_channel.send(embed=embed)
        #await ctx.respond(message_link.content)

def setup(bot):
    """
    Required.
    """
    bot.add_cog(GeneralPin(bot))

def embed_pin(some_message):
    """
    Embedding for user pinning channel
    """
    embed = discord.Embed(
        title=f'Original Message'
        , description=f'{some_message.content}'
        , color=discord.Color.dark_green()
        , url=some_message.jump_url
        , timestamp=some_message.created_at
    )
    embed.add_field(
        name='Sent in:'
        , value=f'{some_message.channel.jump_url} by {some_message.author}'
        , inline=True
    )
    #.replace(microsecond=0)
    return embed
