from detect import detect_text, new_screen
from requests import post
import datetime
import time
import os


def run_api(value):
    url = "http://192/api/states/input_number.tempv" #
    headers = {
        "Authorization": "", #
        "content-type": "application/json",
    }

    data = {"state": value, "attributes": {"unit_of_measurement": "kWh"}}

    response = post(url, headers=headers, json=data)
    print("New value send Home Assistant")
    # print(response.text)


check_value = '06:00:00'

while True:
    x = datetime.datetime.now()
    date_now = x.strftime("%H:%M:%S")

    if date_now == check_value:
        print("Now run detect value")

        new_screen()
        value = detect_text('images/cc.png')
        run_api(value)

        time.sleep(5)






























