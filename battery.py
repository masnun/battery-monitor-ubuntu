#!/usr/bin/env python

import commands
import pynotify
from threading import Timer


def battery_check():

	rem = float(commands.getoutput("grep \"^remaining capacity\" /proc/acpi/battery/BAT0/state | awk '{ print $3 }'"))
	full = float(commands.getoutput("grep \"^last full capacity\" /proc/acpi/battery/BAT0/info | awk '{ print $4 }'"))
	state = commands.getoutput("grep \"^charging state\" /proc/acpi/battery/BAT0/state | awk '{ print $3 }'")

	percentage = int((rem/full) * 100)

	if state == "discharging":
		pynotify.init("Battery Alert!")
		notification = pynotify.Notification("Battery "+state,str(percentage)+"%","/usr/share/icons/gnome/32x32/status/battery-low.png")
		notification.show()

	timer = Timer(300.0,battery_check)
	timer.start()

if __name__ == "__main__": battery_check()
