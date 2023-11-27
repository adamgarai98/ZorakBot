"""
A simple dadjoke command.
"""
import json
import logging
import requests
from discord.ext import commands

logger = logging.getLogger(__name__)


class GeneralOCR(commands.Cog):
    """
    # Hits the icanhazdadjoke API and returns the response
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def ocr(self, ctx, image_url):
        """
        Sends a dad joke using an API
        """
        logger.info("%s used the %s command."
                    , ctx.author.name
                    , ctx.command)
        payload = {"url": image_url
                   , "apikey": "K84818514588957"}
        r = requests.post("https://api.ocr.space/parse/image"
                          , data=payload
                          , timeout = 60
                          )
        await ctx.respond(json.loads(r.content.decode())["ParsedResults"][0]["ParsedText"])
        # await ctx.respond(
        #     json.loads(requests.get("https://icanhazdadjoke.com/", timeout=5, headers={"Accept": "application/json"}).text)["joke"]
        # )


def setup(bot):
    """
    Required.
    """
    bot.add_cog(GeneralOCR(bot))
