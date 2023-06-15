from detect import detect_text, new_screen
from requests import post
import datetime
import time
from logger import logger
from config import *


def run_api(value):
    headers = {
        "Authorization": AUTHORIZATION,
        "content-type": "application/json",
    }

    data = {"state": value, "attributes": {"unit_of_measurement": "kWh"}}

    response = post(BASE_URL, headers=headers, json=data)
    logger.info("New value send Home Assistant")


while True:
    date_now = datetime.datetime.now().strftime("%H:%M:%S")
    # logger.info(date_now)

    if date_now == HOUR:
        logger.info("Now run detect value")
        new_screen()
        value = detect_text('images/capture.png')
        logger.info(value)
        run_api(value)

        time.sleep(5)
