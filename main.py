#from detect import detect_text, new_screen
from requests import post
import datetime
import time
from logger import logger
from config import *

File_object = open(r"value.txt", "r+")
print(int(File_object.read()))
File_object.close()

File_object = open(r"value.txt", "w")
File_object.close()

File_object = open(r"value.txt", "r+")
File_object.write("139")
File_object.close()

File_object = open(r"value.txt", "r+")
print(File_object.read())
File_object.close()

def run_api(value, value_sub):
    headers = {
        "Authorization": AUTHORIZATION,
        "content-type": "application/json",
    }

    data = {"state": value_sub, "attributes": {"unit_of_measurement": "dm3"}}

    response = post(BASE_URL, headers=headers, json=data)

    data = {"state": value, "attributes": {"unit_of_measurement": "dm3"}}
    response = post(URL_SUM, headers=headers, json=data)
    logger.info("New value send Home Assistant")


run_api(501.1, 4)
"""
while True:
    date_now = datetime.datetime.now().strftime("%H:%M:%S")
    # logger.info(date_now)

    if date_now == HOUR:
        logger.info("Now run detect value")
        new_screen()
        value = detect_text('images/capture.png')
        value_sub = value - value_sub
        logger.info(value, value_sub)
        run_api(value, value_sub)

        time.sleep(5)
"""
