
#! -*- coding: utf-8 -*-
#
import subprocess
import os
import os.path

from i3pystatus import Status
from i3pystatus.updates import pacman, cower


status = Status()

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week

status.register("updates",
    format = "Updates: {count}",
    format_no_updates = "",
    on_leftclick="termite --geometry=1200x600 --title=updates -e 'pacaur --needed --noconfirm --noedit -Syu'",
    backends = [pacman.Pacman(), cower.Cower()])

status.register("clock",
    format="%H:%M:%S",
    color='#C678DD',
    interval=1,
    on_leftclick="/usr/bin/gsimplecal",)

status.register("clock",
    format="%a %d-%m-%Y ",
    color='#61AEEE',
    interval=1,)


# status.register("pulseaudio",
#     color_unmuted='#FFFFFF',
#     format="Volume: {volume}%")

#status.register("network",
#    interface="eno1",
#    color_up="#8AE234",
#    color_down="#EF2929",
#    format_up=": {v4cidr}",
#    format_down="",)

# status.register("network",
#     interface="wlan",
#     color_up="#8AE234",
#     color_down="#EF2929",
#     format_up="{essid} {kbs} kbs",
#     format_down="",)

# status.register("backlight",
#     interval=5,
#     format="{percentage:.0f}%",
#     backlight="intel_backlight",)


status.register("battery",
    battery_ident="BAT1",
    interval=5,
    format="Battery: {percentage:.0f}% | {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=15,
    color="#FFFFFF",
    critical_color="#FF1919",
    charging_color="#E5E500",
    full_color="#D19A66",
    status={
        "DIS": "DIS",
        "CHR": "CHR",
        "FULL": "FULL",
},)

status.register("temp",
    color='#78EAF2',
                )

status.register("cpu_usage",
    on_leftclick="termite --title=htop -e 'htop'",
    format="CPU {usage}%",)

status.register("mem",
    color="#FFFFFF",
    warn_color="#E5E500",
    alert_color="#FF1919",
    format="RAM {used_mem}/{total_mem} GB",
    divisor=1073741824,)



    # status.register("text",
    #     text="|",
    #     color="#222222")
status.register("disk",
    color='#FFFFFF',
    path="/",
    format="Disk: {used}/{total} GB",)

# status.register("disk",
#     hints = {"separator": False, "separator_block_width": 3},
#     color='#ABB2BF',
#     path="/run/media/ilya",
#     format="SD: {avail} GB",)
#status.register('ping',
#    format_disabled='',
#    color='#61AEEE')

# status.register("keyboard_locks",
#     format='{caps} {num}',
#     caps_on='Caps Lock',
#     caps_off='',
#     num_on='Num On',
#     num_off='',
#     color='#e60053',
#     )

# status.register("mpd",
#     host='localhost',
#     port='6600',
#     format="{status}",
#     on_leftclick="switch_playpause",
#     on_rightclick=["mpd_command", "stop"],
#     on_middleclick=["mpd_command", "shuffle"],
#     on_upscroll=["mpd_command", "next_song"],
#     on_downscroll=["mpd_command", "previous_song"],
#     status={
#         "pause": " ",
#         "play": " ",
#         "stop": " ",
#     },)

status.run()