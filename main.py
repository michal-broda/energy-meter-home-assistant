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

    data = {"state": value}
    response = post(URL_SUM, headers=headers, json=data)
    logger.info("New value send Home Assistant", value)


while True:
    date_now = datetime.datetime.now().strftime("%H:%M:%S")
    # logger.info(date_now)

    if date_now == HOUR:
        logger.info("Now run detect value")
        new_screen()
        new_value = detect_text('images/test2.png') / 10
        if new_value:
            run_api(new_value)
        else:
            logger.error("New value in HA is not available")

        time.sleep(5)
