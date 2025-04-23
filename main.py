from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from . import ykt_handler
import requests
import json

@register("UJS Assis", "Cacciatore", "A UJS bot assis", "1.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """Construct"""
    
    @filter.command("bill")
    async def get_room_bill(self, event: AstrMessageEvent):

        message_str = event.message_str
        args = message_str.split(" ")
        logger.info(args)
        if len(args) == 2:
            room = str(args[1])
        else:
            room = None

        address, currency, time = ykt_handler.get_room_bill(room)

        result = result = "查询宿舍: {}\n当前余额: {}\n查询时间: {}".format(address, currency, time)

        yield event.plain_result(result)

    async def terminate(self):
        """Desctruct"""