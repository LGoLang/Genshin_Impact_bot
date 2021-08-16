from nonebot import on_command
from nonebot.adapters import Bot, Event

import gacha


genshin_impact_bot_help = on_command("原神帮助")

help_txt = '''这是一个HoshinoBot和nonebot2的原神相关插件，包含原神抽卡，丘丘语翻译，找资源点等功能
插件仓库在 https://github.com/H-K-Y/Genshin_Impact_bot.git

指令：

@bot相遇之缘：10连抽卡
@bot纠缠之缘：90连抽卡
@bot原之井：180连抽卡
原神卡池：查看当前UP池，这个指令也可以用来重载卡池配置文件，config.json保存的是当前卡池信息
原神卡池切换：切换其他原神卡池

丘丘一下 丘丘语句 ：翻译丘丘语,注意这个翻译只能把丘丘语翻译成中文，不能反向
丘丘词典 丘丘语句 ：查询丘丘语句的单词含义

XXX哪里有：查询XXX的位置图，XXX是资源的名字
原神资源列表：查询所有的资源名称

圣遗物收集
原神副本 ： 查询当前有哪些副本，掉落哪个套装  
刷副本 副本名称 ： 刷一次副本，可获得狗粮点数和圣遗物  
查看圣遗物仓库 1 ： 查询仓库第一页有哪些圣遗物  
强化圣遗物10级 5 ： 把仓库编号为5的圣遗物强化10级  
圣遗物洗点 5 ： 把仓库编号为5的圣遗物洗点，洗点后返还50%的强化点数，强化等级降为0，全属性重新随机  
圣遗物详情 5 ： 查看圣遗物详情
转换狗粮 5 ： 把仓库编号为5的圣遗物销毁转化为狗粮，会返还80%狗粮点数  
查看体力值 ： 查看自己体力值  
氪体力 @群友 ： 给群友氪体力，这个命令只有机器人管理员才能执行  

原神黄历
原神黄历 ： 查看今天的黄历
原神抽签 ： 抽一签
解签 ： 解答抽签结果
开启\关闭原神黄历提醒  ： 开启或关闭本群的每日黄历提醒

原神每日材料提醒
今日武器突破材料  ： 查看今日武器突破材料  
今日角色天赋材料  ： 查看今日角色天赋材料  
今日材料  ： 查看今天的武器突破材料和角色天赋材料  
开启\关闭原神每日素材提醒  ： 开启或关闭本群的每日素材提醒  
'''


@genshin_impact_bot_help.handle()
async def genshin_impact_bot_help_(bot: Bot, event: Event):
    await genshin_impact_bot_help.finish(help_txt)
