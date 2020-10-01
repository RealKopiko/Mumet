#! usr/local/bin/python3

import requests
import json
import time
import datetime

parameter = {
    "city": "singapore",
    "country": "singapore"
}

singaporeinfo = requests.get("http://api.aladhan.com/v1/timingsByCity/:date_or_timestamp", params=parameter)
prayertime = singaporeinfo.json()["data"]["timings"]
remove_keys = ["Sunrise", "Sunset", "Imsak", "Midnight"]
for key in remove_keys:
    del prayertime[key]

print(prayertime["Asr"])
Asr_e = time.mktime(datetime.datetime.strptime(prayertime["Asr"], "%H:%M").timetuple())
print(Asr_e)

t = time.localtime()

current_time = time.strftime("%H:%M", t)
print(current_time)


t > Asr_e