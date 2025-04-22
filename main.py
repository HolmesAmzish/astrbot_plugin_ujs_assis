from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from . import ykt_handler

@register("UJS Assis", "Cacciatore", "A UJS bot assis", "1.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    
    @filter.command("bill")
    async def get_room_bill(self, event: AstrMessageEvent):
        """Query the number of online players"""
        
        address, currency, time = ykt_handler.get_room_bill()

        result = result = "查询宿舍: {}\n当前余额: {}\n查询时间: {}".format(address, currency, time)

        yield event.plain_result(result)

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""