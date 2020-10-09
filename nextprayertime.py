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

t = time.localtime()
current_time = time.strftime("%H:%M", t)

print("Next prayer time:")

if current_time <= prayertime["Fajr"]:
    print("Fajr @ " + prayertime["Fajr"])
else:
    if current_time <= prayertime["Dhuhr"]:
        print("Dhuhr @ " + prayertime["Dhuhr"])
    else:
        if current_time <= prayertime["Asr"]:
            print("Asr @ " + prayertime["Asr"])
        else:
            if current_time <= prayertime["Maghrib"]:
                print("Maghrib @ " + prayertime["Maghrib"])
            else: 
                print("Isha @ " + prayertime["Isha"])

