# Ported By @disinikazu & @Riizzvbss
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# ReCode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de


import time
from datetime import datetime

from speedtest import Speedtest

from . import (
     StartTime,
     kazu_cmd,
     DEVLIST,
     eor,
     humanbytes,
     devs_cmd,
     )
from time import sleep


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@kazu_cmd(pattern=r"^pink$", incoming=True, from_users=DEVLIST)
@devs_cmd(incoming=True, from_users=DEVLIST, pattern=r"^Cpink$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ping = await eor(ping, "**✧**")
    await ping.edit("**✧✧**")
    await ping.edit("**✧✧✧**")
    await ping.edit("**✧✧✧✧**")
    await ping.edit("**✧✧✧✧✧**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await ping.edit("⚡")
    sleep(3)
    await ping.edit(
        f"**✧ 𝙺𝙰𝙽𝙴 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 ✧**\n\n"
        f"✧ **𝙿𝙸𝙽𝙶𝙴𝚁 :** `%sms`\n"
        f"✧ **𝚄𝙿𝚃𝙸𝙼𝙴 :** `{uptime}` \n"
        f"✧ **𝙾𝚆𝙽𝙴𝚁 :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


@kazu_cmd(pattern="ping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xping = await eor(ping, "`Pinging....`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xping.edit(
        f"**PONG!! 🍭**\n**Ping** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


@kazu_cmd(pattern="lping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    lping = await eor(ping, "**★ PING ★**")
    await lping.edit("**★★ PING ★★**")
    await lping.edit("**★★★ PING ★★★**")
    await lping.edit("**★★★★ PING ★★★★**")
    await lping.edit("**✦҈͜͡➳ PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await lping.edit(
        f"❃ **Kane Ping !!** "
        f"`%sms` \n"
        f"❃ **Uptime -** "
        f"`{uptime}` \n"
        f"**✦҈͜͡➳ Master :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )


# .keping & kping Coded by Koala
